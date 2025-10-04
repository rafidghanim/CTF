package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"errors"
)

func pad(b []byte, blockSize int) []byte {
	padSize := blockSize - (len(b) % blockSize)
	out := make([]byte, len(b)+padSize)
	copy(out, b)
	for i := range padSize {
		out[len(out)-1-i] = byte(padSize)
	}
	return out
}

func unpad(b []byte, blockSize int) ([]byte, error) {
	if len(b) == 0 {
		return nil, Error("gimme something to unpad")
	}

	padSize := int(b[len(b)-1])
	if padSize == 0 || padSize > blockSize || padSize > len(b) {
		return nil, Error("funky padding")
	}

	for i := range padSize {
		if b[len(b)-1-i] != byte(padSize) {
			return nil, Error("invalid pkcs7 padding")
		}
	}

	return b[:len(b)-padSize], nil
}

func cbcEncrypt(key, msg []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	blockSize := block.BlockSize()

	iv := make([]byte, blockSize)
	check1(rand.Read(iv))

	crypter := cipher.NewCBCEncrypter(block, iv)

	padded := pad(msg, blockSize)
	out := make([]byte, len(padded)+len(iv))
	copy(out, iv)
	crypter.CryptBlocks(out[len(iv):], padded)

	return out, nil
}

func cbcDecrypt(key, cmsg []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	blockSize := block.BlockSize()

	if len(cmsg) < blockSize {
		return nil, errors.New("buf small")
	}

	iv := cmsg[:blockSize]
	cmsg = cmsg[blockSize:]

	decrypter := cipher.NewCBCDecrypter(block, iv)

	out := make([]byte, len(cmsg))
	decrypter.CryptBlocks(out, cmsg)

	return unpad(out, blockSize)
}
