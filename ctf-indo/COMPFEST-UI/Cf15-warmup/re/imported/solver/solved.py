import importlib

filename = "law.py"

def remove_lines(filename, start_line, count):
    with open(filename, "r") as file:
        lines = file.readlines()

    if len(lines) >= start_line + count:
        del lines[start_line - 1 : start_line - 1 + count]

    with open(filename, "w") as file:
        file.writelines(lines)

while True:
    module = importlib.import_module("law")
    output = ""

    importlib.reload(module)
    char = module.c()
    output += char
    flag = char
    print(f"{flag}",end="", flush=True)

    if char == "}":
        print()
        break

    # Remove lines 16 and 17
    remove_lines(filename, 14, 2)

print(output)
