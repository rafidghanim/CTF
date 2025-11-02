function reverseXOR(encryptedMessage, key) {
  let decryptedMessage = '';

  for (let i = 0; i < encryptedMessage.length; i++) {
    // XOR kembali setiap elemen dengan kunci
    const decryptedChar = String.fromCharCode(encryptedMessage[i] ^ key);
    decryptedMessage += decryptedChar;
  }

  return decryptedMessage;
}

// Contoh penggunaan
const encryptedMessage = [140, 132, 180, 148, 200, 170, 179, 139, 163, 255, 163, 177, 171, 191, 180, 208, 230, 147, 234, 206];
const key = 1337;

const decryptedMessage = reverseXOR(encryptedMessage, key);
console.log(decryptedMessage);
