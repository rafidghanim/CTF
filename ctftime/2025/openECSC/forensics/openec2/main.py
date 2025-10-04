#!/usr/bin/env python3
import pathlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
i = __import__
key = i("\x62\x61\x73\x65\x36\x34").urlsafe_b64encode(PBKDF2HMAC(hashes.SHA256(),0o40,bytes.fromhex(pathlib.Path("\x2f\x65\x74\x63\x2f\x6d\x61\x63\x68\x69\x6e\x65\x2d\x69\x64").read_text()),0o46113200,).derive(input("\x50\x61\x73\x73\x77\x6f\x72\x64\x3a\x20").strip().encode()))
c = Fernet(key)
code = i("\x6d\x61\x72\x73\x68\x61\x6c").loads(c.decrypt(pathlib.Path("\x63\x6f\x64\x65\x2e\x62\x69\x6e").read_bytes()))
# conf = json.loads(c.decrypt(pathlib.Path("\x63\x6f\x6e\x66\x69\x67\x2e\x62\x69\x6e").read_bytes()))
print(code)
