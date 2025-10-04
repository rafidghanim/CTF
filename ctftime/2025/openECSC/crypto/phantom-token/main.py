#!/usr/bin/env python3

import msgpack
from flask import Flask, request
import hmac
import hashlib
import secrets
import os

app = Flask(__name__)

hmac_secret = secrets.token_bytes(32)
hmac_algo = hashlib.md5


def digest(msg: bytes) -> bytes:
    return hmac.digest(hmac_secret, msg, hmac_algo)


@app.route("/hmac")
def gethmac():
    return hmac_secret


@app.route("/token", methods=["POST"])
def getuser():
    user = request.get_data() or b"user"

    if len(user) > 128 or user == b"admin":
        user = b"nicetry"

    mac = digest(user)

    return msgpack.dumps({"u": user, "m": mac})


@app.route("/flag", methods=["POST"])
def getflag():
    try:
        return _getflag()
    except Exception as e:
        return str(e)


def _getflag() -> str:
    encoded = request.get_data()
    try:
        data = msgpack.loads(encoded)
    except Exception as e:
        return f"error unpacking: {e}"
    if type(data) != dict:
        return f"not a dict: {data}"

    mac = data.get("m", b"")
    user = data.get("u", b"")

    if not mac:
        return "missing mac"

    if not user:
        return "missing user"

    # expensive validation moved to proxy
    """
    if not hmac.compare_digest(digest(user), mac):
        return "mac mismatch"
    """

    if user == b"admin":
        return os.environ.get("FLAG", "ctf{placeholder}")

    return f"hello, {user}"
