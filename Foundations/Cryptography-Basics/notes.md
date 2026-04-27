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

## RSA Encryption

- An asymmetric encryption algorithm that uses public and private keys.
- RSA is a computationally expensive algorithm, so it is frequently used for the creation of symmetric keys rather than encrypting large amounts of data itself. 
- Uses a one-way function based on modular arithmetic. 

### Mathematical Principles

Choose two very large prime numbers, p and q. Then compute, 

n=p*q 

where n is the mod value. 

L = (p-1)*(q-1) where L is the "length", which represents the number of values between 1 and n that do not have any common factors. Also typically denoted as phi(n).

Find a value, e, such that e is between 1 and L and the greatest common factor between all three is 1. 

Find a value, d, such that d*e = 1 mod(L)

The public key is (n,e)

The private key is (n,d)

Encryption formula: c = m^e mod (L) where m is the message and c is the ciphertext. 

Decryption formula: m = c^d mod (L) where c is the ciphertext and m is the message. 

### Example

Let's encrypt the letter "h" using a simple RSA example. In this example, we will assign numbers to each letter as they appear in alphabetical order (i.e., a=1, b=2, ...) and we will use small prime numbers to keep it simple. In reality, this process would use two very large prime numbers and typically ASCII to encode the letters. 

Since h is the 8th letter of the alphabet we will say that h = 8.

Now, choose two prime numbers, say p=2 and q=11. So, n=p\*q so n=2\*11 = 22. 

Calculate L: L = (p-1)\*(q-1) = (2-1)\*(11-1) = (1)\*(10) = 10. 

Find a value, e, such that e is between 1 and 10 and the greatest common factor between all three is 1. In this case, let e = 7. 

Find a value, d, such that d\*e = 1 mod(L), so d\*7 mod (10) = 1. If d = 3, then 3\*7 = 21 and 21 = 2\*10 + 1. Note: it is possible for there to be a range of values for d, which is part of what makes RSA hard to break. 

Now, we encrypt the message h=8:

In this case our message, m will be 8. So, c = 8^7 mod (10) = 2097152 mod (10) = 2

So, our encrypted message is: 2

Now, we decrypt the message using c=2:

m = 2^3 mod (10) = 8 mod (10) = 8

And, we know that 8=h so we have figured out the original message!

## HMAC

- HMAC stands for Hash-based Message Authentication Code and is used to verify the integrity of messages.
- Uses a cryptographic hash function and a shared secret key. 
- Both the sender and receiver have the shared secret key. 
- The cryptographic hash uses various algorithms such as MD-5, SHA256 or SHA512. 
- HMAC is symmetric.

### Process

- HMAC follows a general formula: HMAC = hash_function(secret_key + message) = hash_function(K,m) = hash_function((K (XOR) opad) || hash_function((K (XOR) ipad) || m))
- Alice and Bob want to share private messages, making sure that the messages cannot be changed during transportation. 
- First, Alice and Bob exchange a secret key that they both know. 
- Next, Alice uses the secret key and her message to create a hash value using the HMAC formula. 
- Alice sends the original message and HMAC to Bob.
- Bob uses the same secret key to create an HMAC using the message. 
- Bob checks to see if his HMAC matches the one Alice sent. If they match, the message remained intact during transportation. If they do not match, this means the message was altered and the integrity of the message fails. 

### Example

Let's do a simple example using a very small block size (4 bytes), and a very small message only using the letter "A":

- b = 4, where b represents block size. In this case, our block size is 4. 

- K = x01020304 (in hexadecimal).

- message = "A" = 0x41 (in hexademical) = 65 (in decimal) = 01000001 (in binary). Use an ASCII table to find the hexadecimal or decimal values for each character. 

ipad = inner padding = 0x36 repeated to the block size

opad = outer padding = 0x5c repeated to the block size

ipad and opad are fixed values defined by the HMAC standard, meaning you will always use these values. It is similar idea to how pi always equals 3.14...

- ipad = x36363636 (in hexadecimal), repeated 4 times because we are only using 4 bytes. We will represent as ipad = 36 36 36 36 for easier reading here.

- opad = x5c5c5c5c (in hexadecimal), repeated 4 times because we are only using 4 bytes. We will represent as opad = 5c 5c 5c 5c for easier reading here.

Helpful note: 

36 = 00110110 in binary

5c = 01011100 in binary

- Check if key is exactly the same as the block size. If not, adjust as follows:

- In our case, K = x01020304 which is already 4 bytes (01 02 03 04). No adjustment needed.

Let's do two examples showing what to do if this was not the case:

1. K `<` b. 

Let's say K=0102. In this case, K is only 2 bytes. 

We create a new key, K1, and pad it with zeros until it matches the required 4 bytes: K1 = 01020000

Now, we can proceed with the algorithm

2. K `>` b.

Let's say K=010203040506. In this case, K is 6 bytes. 

First, we must hash the existing key, K. If you were using SHA256, you would use this on K. However, for our simple example, pretend our chosen hash (we will call it hash256) performs this by doing the following:

01 + 02 + 03 + 04 + 05 + 06 = 21

Convert 21 to hexadecimal: 0x15

Now, our new key, K1 = 0x15. However, this is too short. So, we must pad it with zeros until it matches the required 4 bytes: K1 = 15000000

Now, we can proceed with the algorithm

- In our case, K is already 4 bytes so we do not change it. 

- Next, we perform the XOR operation on K with ipad. XOR stands for exclusive OR and has the following rules:

0 XOR 0 = 0

0 XOR 1 = 1

1 XOR 0 = 1

1 XOR 1 = 0

Essentially, XOR follows the rules of OR gate logic except it "excludes" the case where both bits are the same, i.e., both bits are 1. 

- Perform XOR on K with ipad (I will do this in binary for easier visualization):

K = 0001000000100000001100000100. We can separate it by bytes for easier reading: 00000001 00000010 00000011 00000100

ipad = 00110110 00110110 00110110 00110110

- XOR 00000001 with 00110110 which gives: 00110111 = 37 in hex

- XOR 00000010 with 00110110 which gives: 00110100 = 34 in hex

- XOR 00000011 with 00110110 which gives: 00110101 = 35 in hex

- XOR 00000100 with 00110110 which gives: 00110010 = 32 in hex

So, K (XOR) ipad = 37343532 = 00110111001101000011010100110010

- Next, append the message with: (K (XOR) ipad) || m, where || means concatenate the values (in some contexts || means the OR operation, so it is important to remember in this context is does not mean this).

- Recall our message, m=0x41 which is 01000001 in binary.

- Concatenate: 37343532||41 = 3734353241 or in binary: 00110111001101000011010100110010||01000001 = 0011011100110100001101010011001001000001

All you have to do here is stick the values together like glue. 

- Next, we put this result into our hash. For example, if you were using SHA256, you would use the SHA256 hash on this result. For our simple example, we will again use our pretend hash, hash256, as follows:

First we convert the hexadecimal values to decimal for adding:

37 (hex) = 55 (decimal), 34 (hex) = 52 (dec), 35 (hex) = 53 (dec), 32 (hex) = 50 (dec), 41 (hex) = 65 (dec)

Now add: 55+52+53+50+65 = 275 (in decimal)

Next step of hash256 is mod operation: 275 mod (256) = 19 (in decimal)

Convert 19 back to hexadecimal and/or binary: hash_result = 0x13 (hex) = 00010011 (binary)

- Next, perform XOR on K and opad: 

K = 001000000100000001100000100. We can separate it by bytes for easier reading: 00000001 00000010 00000011 00000100

opad = 01011100 01011100 01011100 01011100

- XOR 00000001 with 01011100 which gives: 01011101 = 5d in hex

- XOR 00000010 with 01011100 which gives: 01011110 = 5e in hex

- XOR 00000011 with 01011100 which gives: 01011111 = 5f in hex

- XOR 00000100 with 01011100 which gives: 01011000 = 58 in hex

So, K (XOR) opad = 5d5e5f58 = 01011101010111100101111101011000

- Next, append the hash_result with: (K (XOR) opad) || hash_result

- Concatenate: 5d5e5f58||13 = 5d5e5f58 (in hexadecimal) or in binary: 01011101010111100101111101011000||00010011 = 0101110101011110010111110101100000010011

Next, we put this new result into our hash:

First convert to decimal for adding:

5d (hexadecimal) = 93 (decimal), 5e (hex) = 94 (dec), 5f (hex) = 95 (dec), 58 (hex) = 88 (dec), 13 (hex) = 19 (dec)

Now add: 93+94+95+88+19 = 389

Next step of our example, hash256, is mod operation: 389 mod 256 = 133 (in decimal) = 85 (in hexadecimal)

Final HMAC: 0x85 

Now, Bob computes the HMAC using the same secret key and if his final HMAC matches the one from Alice, then the message was not altered in transportation and its integrity is sound. 

## AES Encryption

- AES stands for Advanced Encryption Standard. 
- AES is a symmetric block cipher that uses the same key for both encryption and decryption. 
- The key lengths vary but are typically 128,192,256 bits. 
- The encryption data is always done in blocks of 128 bits. 

### Overview

- It is impractical to do any AES example by hand, but the process is performed as follows:

Step 1: Input data

- The input data is processed in 128 bits at a time.

- The number of rounds depends on key length:

| N (rounds) | key size (bits) |
| ---------- | --------------- |
| 10 | 128 |
| 12 | 192 |
| 14 | 256 | 

Step 2: Round key creation

- The original key is used to create each of the different round keys which are used at each corresponding round of the encryption.
- Essentially, you use the one original key to create many different keys. 

Step 3: Encryption

- Each block is a 16 byte grid (4 rows of 4 bytes each, or 4x4 bytes = 128 bits).
- Each round of encryption has 4 steps: SubBytes, ShiftRows, MixColumns, Add Round Key 

Step 3.1: SubBytes

- SubBytes means substitution. 
- Each byte is replaced using a lookup table, typically known as the S-box. 

Step 3.2: ShiftRows

The rows of each 4x4 byte grid are shifted as follows:

- Row 0: not shifted 
- Row 1: shift left by 1 (for example: \[byte4, byte5, byte6, byte7\] = \[byte5, byte6, byte7, byte4\])
- Row 2: shift left by 2
- Row 3: shift left by 3

Step 3.3: MixColumns

- This step performs matric multiplication. 
- Each column is multiplied with a specific matrix which changes the position of each byte in the column.
- This step is not performed in the last round.
- The specific matrices that each column is multiplied with are standard: 

| 2 3 1 1 |

| 1 2 3 1 |

| 1 1 2 3 |

| 3 1 1 2 |

The multiplication is performed as follows: 

- \[col0\] = \[byte0_column\] * \[2 3 1 1\]

- \[col1\] = \[byte1_column\] * \[1 2 3 1\]

- \[col2\] = \[byte2_column\] * \[1 1 2 3\]

- \[col3\] = \[byte3_column\] * \[3 1 1 2\]

Step 3.4: Add Round Key

- The previous result (in the format of just 128bits rather than a 4x4 byte grid) is XOR'ed with the corresponding round key. 

Step 4: Repeat step 3 many times (for the total number of rounds). 

- This ensures that the encryption is difficult to break. 

Step 5: Decryption

- The same process is done as encryption, except in the reverse order using the same key, with a few small differences:

Step 5.2: Inverse MixColumns

- Here, there is also a specific matrix used to multiply, except this time it is:

| 14 11 13 9 |

| 9 14 11 13 |

| 13 9 14 11 |

| 11 13 9 14 |

The multiplication is performed as follows:

- \[byte0_col\] = \[14 11 13 9\] * \[col0\]

- \[byte1_col\] = \[9 14 11 13\] * \[col1\]

- \[byte2_col\] = \[13 9 14 11\] * \[col2\]

- \[byte3_col\] = \[11 13 9 14\] * \[col3\]

Step 5.4: Inverse SubBytes

- In this step, Inverse S-box is used as the lookup table instead of S-box.

Special Notes:

- The fixed matrices used in each MixColumns step are chosen using a specific mathematical system to ensure that the chosen inverse matrices can quickly reverse (undo) the multiplication that was done in the original MixColumns step. This is why the numbers used in the forward direction differ from those used in the inverse direction. The forward numbers, which are combinations of the values 1,2,3 were chosen because they are easy and fast to compute in hardware. The inverse numbers, which are combinations of the values 9,11,13,14 were calculated using the mathematical system as the exact values that quickly undo the original operations. 