const fs = require('fs');

// Read the encoded string from the file
fs.readFile('enc.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  // Trim any leading/trailing whitespace or line breaks from the content
  const encodedString = data.trim();

  // Apply the reverse decoding process
  let encArray = encodedString.split("").map(char => char.charCodeAt(0));

  let holder1 = [];
  let holder2 = [];
  let flagLength = encArray.length / 2;

  encArray.forEach((value, index) => {
    if (index === 0) {
      holder1[index] = value - 1;
    } else {
      holder1[index] = (encArray[index] - encArray[index - 1] + (2**9<<16)) % (2**9<<16);
    }
  });

  holder1.forEach((value, index) => {
    if (index === 0) {
      holder2[index] = holder1[index];
    } else {
      holder2[index] = (value - holder1[index - 1] + (2**9<<8)) % (2**9<<8);
    }
  });

  let decodedArray = [];
  holder1.forEach((value) => {
    decodedArray.push(value);
  });
  holder2.forEach((value) => {
    decodedArray.push(value);
  });

  let decodedString = decodedArray.map(code => String.fromCharCode(code)).join("");

  console.log(decodedString);
});
