package main

import (
	"fmt"
	"slices"
)

func msgpackGet(b []byte, key string) ([]byte, error) {
	var off int
	// outer must be map
	if len(b) == 0 {
		return nil, Error("empty buffer")
	}

	if b[0]&0xf0 != 0x80 {
		return nil, Error("outer must be fixmap")
	}

	numPairs := b[0] & 0xf
	off++

	for range numPairs {
		var pairKey string
		var pairValue []byte
		var err error
		pairKey, off, err = msgpackParseStr(b, off)
		if err != nil {
			return nil, err
		}
		pairValue, off, err = msgpackParseBytes(b, off)
		if err != nil {
			return nil, err
		}
		if pairKey == key {
			return pairValue, nil
		}
	}

	return nil, fmt.Errorf("key not present: %s", key)
}

func msgpackParseStr(b []byte, off int) (string, int, error) {
	if len(b)-off < 1 {
		return "", len(b), Error("short read on string type")
	}

	strTyp := b[off]
	off++
	if strTyp&0xe0 == 0xa0 {
		// fixstr
		strLen := int(strTyp & 0x1f)
		if len(b)-off < strLen {
			return "", len(b), Error("fixstr length too large")
		}

		str := string(b[off : off+strLen])
		off += strLen
		return str, off, nil
	}

	switch strTyp {
	case 0xd9:
		// str 8
	case 0xda, 0xdb:
		return "", len(b), Error("unsupported large string type")
	default:
		return "", len(b), Error("unexpected non-string key type")
	}

	if len(b)-off < 1 {
		return "", len(b), Error("str 8 short")
	}

	strLen := int(b[off])
	off++
	if len(b)-off < strLen {
		return "", len(b), Error("str 8 length too large")
	}

	str := string(b[off : off+strLen])
	off += strLen
	return str, off, nil
}

func msgpackParseBytes(b []byte, off int) ([]byte, int, error) {
	if len(b)-off < 1 {
		return nil, len(b), Error("short read on binary type")
	}
	binTyp := b[off]
	off++
	switch binTyp {
	case 0xc4:
		// bin 8
	case 0xc5, 0xc6:
		return nil, len(b), Error("unsupported large binary type")
	default:
		return nil, len(b), Error("unexpected non-string value type")
	}

	if len(b)-off < 1 {
		return nil, len(b), Error("bin 8 short")
	}

	binLen := int(b[off])
	off++
	if len(b)-off < binLen {
		return nil, len(b), Error("bin 8 length too large")
	}

	bin := slices.Clone(b[off : off+binLen])
	off += binLen
	return bin, off, nil
}
