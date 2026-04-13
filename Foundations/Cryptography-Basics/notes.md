# Cryptography Notes

## Symmetric vs Asymmetric Encryption

### Symmetric Encryption

- Requires a shared private key to be shared between parties.
- The same key that is used to encrypt data is also used to decrypt the data.
- Benefits:
    - Withstands frequency analysis:
        - Makes sure that characters do not get mapped in ways that can be detected by pattern recognition.
        - Produces a different output each time, even when the input is identical. 
- Drawbacks:
    - Key management:
        - If you want to share content with someone, you must find a way to securely provide them with the key.
        - If you want to stop sharing content with someone, you must change the key.
- Examples:
    - Caesar Cipher
    - Advanced Encryption Standard (AES)

### Asymmetric Encryption

- Uses two different keys: a public key and a private key.
- The public key is visible to anyone and can be used to encrypt data, while the private key is only visible to those who have access to it.
- Benefits:
    - Key management:
        - No need to provide keys to others - only the owner can decrypt with the private key.
    - Security:
        - Accomplished mathematically with one-way functions which makes it easy to create the keys, but very difficult to figure them out.
        - Because the keys are very large, it is difficult even for computers to reverse-engineer. 
- Drawbacks:
    - Speed:
        - Much slower than symmetric encryption and not suitable for lots of data.
    - Future Vulnerabilities:
        - With breakthroughs in advanced computing (quantum computing), it may become possible to break this encryption type in the future. 
- Examples:
    - Rivest-Shamir-Adleman (RSA)
    - Diffie-Hellman Key Exchange
    - Elyptic Curve Cryptography (ECC)

## Caesar Cipher 

A monoalphabetic letter-to-letter cipher where each letter is shifted by a specified amount. 

### Example

Example: shift by 2

- A = C
- B = D
- C = E
- ...

Phrase to encrypt: hello

Enciphered phrase (shift forward by 2): jgnnq

### Key Concepts

- Original message: plaintext
- Enciphered message: ciphertext
- Key: numerical shift value

### Drawbacks

- Not secure for modern use: only 25 possible keys makes brute force very easy
- Easy to perform frequency analysis

