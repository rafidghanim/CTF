package main

import (
	"bytes"
	"crypto/hmac"
	"crypto/md5"
	"crypto/rand"
	"io"
	"log"
	"net/http"
	"time"
)

var aesKey []byte
var hmacKey []byte

func main() {
	aesKey = make([]byte, 16)
	hmacKey = make([]byte, 32)
	check1(rand.Read(aesKey))
	hmacKey = check1(getHmacKey())

	http.HandleFunc("/token", getToken)
	http.HandleFunc("/flag", getFlag)

	check(http.ListenAndServe(":8000", nil))
}

func getHmacKey() ([]byte, error) {
	var res *http.Response
	var err error
	for range 10 {
		res, err = http.Get("http://flask:5000/hmac")
		if err == nil {
			return io.ReadAll(res.Body)
		}

		time.Sleep(time.Second * 3)
	}

	return nil, err
}

func digest(msg []byte) []byte {
	digester := hmac.New(md5.New, hmacKey)
	digester.Write(msg)
	return digester.Sum(nil)
}

const BLOCKED = "request blocked"

func validateReqBody(req *http.Request) []byte {
	if req.Method != "POST" {
		return nil
	}

	if !(req.ContentLength > 0 && req.ContentLength < (1<<16)) {
		return nil
	}

	body, err := io.ReadAll(req.Body)
	if err != nil {
		return nil
	}

	if bytes.Contains(body, []byte("admin")) {
		return nil
	}

	return body
}

func getToken(w http.ResponseWriter, req *http.Request) {
	body := validateReqBody(req)
	if body == nil {
		log.Print("invalid request body on token")
		w.WriteHeader(http.StatusForbidden)
		w.Write([]byte(BLOCKED))
		return
	}

	resp, err := http.Post("http://flask:5000/token", "application/octet-stream", bytes.NewReader(body))
	if err != nil {
		log.Print("error requesting token")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	respBody, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Print("error reading token")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	encrypted, err := cbcEncrypt(aesKey, respBody)
	if err != nil {
		log.Print("error encrypting token")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Write(encrypted)
}

func getFlag(w http.ResponseWriter, req *http.Request) {
	body := validateReqBody(req)
	if body == nil {
		log.Print("invalid request body on flag")
		w.WriteHeader(http.StatusForbidden)
		w.Write([]byte(BLOCKED))
		return
	}

	decrypted, err := cbcDecrypt(aesKey, body)
	if err != nil {
		log.Print("invalid decryption in flag")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	username, err := msgpackGet(decrypted, "u")
	if err != nil {
		log.Print("could not get u value")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	if bytes.Equal(username, []byte("admin")) {
		log.Print("admin user request detected")
		w.WriteHeader(http.StatusForbidden)
		w.Write([]byte(BLOCKED))
		return
	}

	mac, err := msgpackGet(decrypted, "m")
	if err != nil {
		log.Print("mac not present")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	if !bytes.Equal(mac, digest(username)) {
		log.Print("invalid mac")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	bytes.NewReader(decrypted)

	resp, err := http.Post("http://flask:5000/flag", "application/octet-stream", bytes.NewReader(decrypted))
	if err != nil {
		log.Print("unable to send request to flask")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	respBody, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Print("unable to read response from flask")
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Write(respBody)
}

func check(err error) {
	if err != nil {
		log.Panic(err)
	}
}

func check1[T any](arg1 T, err error) T {
	check(err)
	return arg1
}

type Error string

func (e Error) Error() string {
	return string(e)
}
