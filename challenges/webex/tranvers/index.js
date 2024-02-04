const http = require("http");
const fs = require("fs");
const path = require("path");
const url = require("url");
const svgCaptcha = require("svg-captcha");

const config = require("./config.js");

const captchaStore = {};

const server = http.createServer((req, res) => {
  if (req.url.startsWith("/static/")) {
    const clientIP = req.connection.remoteAddress;
    const captchaInfo = captchaStore[clientIP] || { attempts: 0, captcha: null };

    if (captchaInfo.attempts >= config.maxAttempts) {
      res.writeHead(302, { Location: "/captcha" });
      res.end();
      return;
    }

    const urlPath = req.url.replace(/\.\.\.\.\.\.\.\.\.\.\.\.\.\.\/\/\/\/\//g, "");
    const filePath = path.join(__dirname, urlPath);
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404);
        res.end("Error: File not found");
        console.log(filePath);
      } else {
        captchaInfo.attempts++;
        captchaStore[clientIP] = captchaInfo;

        res.writeHead(200);
        res.end(data);
      }
    });
  } else if (req.url === "/captcha") {
    const clientIP = req.connection.remoteAddress;
    const captchaInfo = captchaStore[clientIP] || { attempts: 0, captcha: null };

    const captcha = svgCaptcha.create();
    captchaInfo.captcha = captcha.text;
    captchaStore[clientIP] = captchaInfo;

    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(`
    <html>
    <head>
      <title>CAPTCHA Page</title>
      <style>
        body {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
        }
  
        h1, p, form {
          text-align: center;
        }
      </style>
    </head>
    <body>
      <div>
        <h1>SUSPICIOUS ATTEMPT DETECTED</h1>
        <p>Your IP address: ${clientIP}</p>
        <img src="data:image/svg+xml,${encodeURIComponent(captcha.data)}" alt="CAPTCHA">
        <form action="/submit-form" method="post">
          <label for="captcha">Enter CAPTCHA:</label>
          <input type="text" id="captcha" name="captcha" required>
          <button type="submit">Submit</button>
        </form>
      </div>
    </body>
  </html>  
    `);
    return;
  } else if (req.url.startsWith("/flag/")) {
    const parsedUrl = url.parse(req.url, true);
    const queryObject = parsedUrl.query;

    if (queryObject.secret === config.secret) {
      res.writeHead(200);
      res.end(config.flag);
    } else {
      res.writeHead(403);
      res.end("Incorrect secret: flag{nope}");
    }
  } else if (req.url === "/submit-form" && req.method === "POST") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
    });

    req.on("end", () => {
      const formData = new URLSearchParams(body);
      const userInputCaptcha = formData.get("captcha");

      const clientIP = req.connection.remoteAddress;
      const captchaInfo = captchaStore[clientIP] || { attempts: 0, captcha: null };

      if (userInputCaptcha && userInputCaptcha === captchaInfo.captcha) {
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(`<html><script>window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';</script></html>`);
        return;
      } else {
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(`<html><script>window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';</script></html>`);
        return;
      }
    });
  } else if (req.url === "/") {
    fs.readFile("index.html", (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end("Error");
      } else {
        res.writeHead(200);
        res.end(data);
      }
    });
  } else {
    res.writeHead(404);
    res.end("404: Resource not found");
  }
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000/");
});
