# save as inspect_obfuscated.py
import base64
import zlib
import marshal
import dis
import sys
import io
import os

# Put only the inner base64 string here (without quotes or trailing paren).
#B64 = """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"""
B64 = """eJxtU89PE0EUnpndLVto2IKQlaihEQUWYxsSE5NqRA7+CMEm6oleJpvuAC1LW2a2YEmJhnDgajxwMCYeMXjgT8Cbx1ZJ2qzePHFr7EHDyZlttxbKJvtm8973vvf2+3Z/gY5Lbp2NCA97wAIWtEESIPAEWGgHWNIBagKSsAgN+UQ8JlKdDNBnuOwxEI60QBJZcAckJcGRlIuSIbv98+kUyTLyzMyaS4SmUAeH1Lob8x5HCZYAbhdLIAO6r4zUnbPgQWsbhubANiwCAyVcZdlx8sxA7qDd3AAzQtcJxQVqu73MManDNtLOMkfIjNiLtMcj4CESOY1Eo7HUsmnbJLtEbjOaii2aJou1mKL5oqtinM6mHYw39bNvGPULQmN2g4c3oHb9zq58rI7WtEtVbbyijVe16Yo2fThxrMXLaryixRti/TPiKL44R544QeD4koNMJ+6/XHJ39j0X5wOyUAmm4ee2qVuohDKBC4SUVyYBoBFeDXZXD/zpfRd0KlbAZ3/Jdy0GxvgXssDPV9IC2IBGT2IzGFs37bRlOsTt8y1ZIUUDunKG5bInX3mvq3iYx0bAVSlZKxDmMFfO55jj2eP2cd+cAsOpnEWoJjLSEnEMiYp9ab9I8D6Wz3FyJnleRmivSIf94bg1e3P0nG/nAarwL+P5V0dKcOCnPrq39XZrX65OzlQmZ8oTD4+C5Ztz5Re4bNrl56vHenb3aU3Tq9pYRRv7yL5pU7Vmy7vXVX2qok/t3z189F2Pl8PxugTCt+oqCA//rSswOFALhWva0CkL8XHbs0OzI+DLCJq9JiUMRXxpWXOVYOz2Yryaswq2eA5hvFYw7WaFCkuozsMnQAWH985U9oNQwuPeAb8RUu411B5luAkUZQPRwTb+ightjlP1fnPkA3oVNP96JrB1CUL4A2h/5BAc/g148Hr+AZYg+fg="""
def main():
    try:
        raw = base64.b64decode(B64)
    except Exception as e:
        print("base64 decode failed:", e); return

    try:
        decompressed = zlib.decompress(raw)
    except Exception as e:
        print("zlib decompress failed:", e); return

    # At this point `decompressed` should be a marshalled code object bytes.
    # We'll use marshal.loads to get the code object but we WILL NOT exec it.
    try:
        code_obj = marshal.loads(decompressed)
    except Exception as e:
        print("marshal.loads failed:", e); 
        # optionally show a hex preview of the bytes
        print("First 200 bytes (hex):", decompressed[:200].hex())
        return

    print("== Disassembly (top-level) ==")
    try:
        dis.dis(code_obj)
    except Exception as e:
        print("disassembly failed:", e)

    print("\n== Code object attributes ==")
    print("co_name:", getattr(code_obj, "co_name", None))
    print("co_filename:", getattr(code_obj, "co_filename", None))
    print("co_argcount:", getattr(code_obj, "co_argcount", None))
    print("co_consts (summary):")
    consts = list(code_obj.co_consts)
    for i, c in enumerate(consts):
        # Only show short reprs to avoid huge binary dumps
        t = type(c).__name__
        if isinstance(c, (str, int, float)):
            print(f"  [{i}] ({t}): {repr(c)[:200]}")
        else:
            print(f"  [{i}] ({t})")

    print("\n== Names & varnames ==")
    print("co_names:", code_obj.co_names)
    print("co_varnames:", code_obj.co_varnames)

    # Optionally save the marshalled bytes and a .pyc-like file for tools
    out_dir = "decoded_out"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "raw_decompressed.bin"), "wb") as f:
        f.write(decompressed)
    print(f"\nWrote raw decompressed bytes to {out_dir}/raw_decompressed.bin")

    # Optionally write a minimal pyc file (so decompilers can read it)
    # Note: .pyc requires a 16-byte header (magic + timestamp/hash). We'll write a simple pyc header.
    try:
        import importlib.util, time, struct
        magic = importlib.util.MAGIC_NUMBER  # python magic for this interpreter
        mtime = int(time.time())
        header = magic + struct.pack("<II", mtime, 0)  # 12 or 16 bytes header depending on py version
        with open(os.path.join(out_dir, "maybe.pyc"), "wb") as f:
            f.write(header)
            f.write(decompressed)
        print(f"Wrote possible pyc to {out_dir}/maybe.pyc")
    except Exception as e:
        print("Could not write pyc header:", e)

if __name__ == "__main__":
    main()
