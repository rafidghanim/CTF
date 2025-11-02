import os
import time
import base64
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_message():
    for i in range(random.randint(50, 80)):
        cls()
        message = base64.b64decode('R2VuZXJhdGluZyB5b3VyIGZsYWcuLi4=').decode("utf-8")
        print(f"{message} {i}")
        time.sleep(0.1)

def calculate_values():
    a = 1
    b = 2
    sum_ab = a + b
    diff_ab = sum_ab - a
    product = diff_ab * b
    division_result = product / a
    exponentiation_result = division_result ** b
    print(base64.b64decode('SXQgY29tZXMgaW4gd2F2ZXMsIEkgY2xvc2UgbXkgZXllcy4gSG9sZCBteSBicmVhdGggYW5kIGxldCBpdCBidXJ5IG1lLiBJJ20gbm90IE9LIGFuZCBpdCdzIG5vdCBhbHJpZ2h0LiBXb24ndCB5b3UgZHJhZyB0aGUgbGFrZSBhbmQgYnJpbmcgbWUgaG9tZSBhZ2Fpbg==').decode("utf-8"))
    return exponentiation_result

def main():
    display_message()
    try:
        calculate_values()
    except Exception as e:
        print("\n\nAn error occurred:", e)

    print("\n\nHere's Your Flag: ")
    flag = base64.b64decode('X3kwdV9kMHdubDA0ZF8wbmwxbjN3MTVfNTRmM30=').decode("utf-8")
    print(flag)

if __name__ == "__main__":
    main()
