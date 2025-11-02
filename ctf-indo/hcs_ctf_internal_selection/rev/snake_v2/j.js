function decrypt(xor_value, integrityCheck) {
  const flag = [0x8c, 0x84, 0xb4, 0x94, 0xc8, 0xaa, 0xb3, 0x8b, 0xa3, 0xff, 0xa3, 0xb1, 0xab, 0xbf, 0xb4, 0xd0, 0xe6, 0x93, 0xea, 0xce];
  let decryptedFlag = "";

  for (let i = 0; i < flag.length; i++) {
    // Balikkan operasi xor
    flag[i] -= integrityCheck;
    flag[i] &= 0xff;
    flag[i] ^= xor_value[i % xor_value.length];

    decryptedFlag += String.fromCharCode(flag[i]);
  }

  return decryptedFlag;
}

// Contoh penggunaan
const xor_value_example = "50px sans-serif"; // Ganti dengan nilai xor yang sesuai
const integrityCheck_example = 0x539; // Ganti dengan nilai integrityCheck yang sesuai

const result = decrypt(xor_value_example, integrityCheck_example);
console.log(result);
