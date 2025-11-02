import importlib

module = importlib.import_module("secret")
output = ""

while True:
    importlib.reload(module)
    char = module.c()
    output += char
    print(".",char, end="", flush=True)

    if char == "}":
        print()
        break

print(output)
