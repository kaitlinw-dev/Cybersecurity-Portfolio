# Cryptography Basics

This folder contains beginner implementations of cryptographic concepts.

## Contents

### Caesar Cipher

- File name: `caesar_cipher.py` 
- Description: A simple substitution cipher that shifts letters by a fixed number, implemented with multiple methods. 
- Purpose: Introduces basic encryption concepts such as plaintext, ciphertext, and keys. 

## How to Run

Make sure you are in the following directory: `Foundations/Cryptography-Basics/`

### Caesar Cipher

```bash
python3 caesar_cipher.py
```

## Purpose 

- Understand the difference between symmetric and asymmetric encryption
- Learn how encryption algorithms transform data
- Explore message integrity using HMAC
- Build a foundation for secure application development

## Notes

Detailed explanations of learning and process can be found in `notes.md`.  

## Credits

The contents of the file entitled `notes.md` contain my notes and learning exercises gained from following the tutorials or articles provided below. I in no way claim any logic or code as my own that was obtained from the tutorials or articles below. These notes and exercises were completed purely for learning purposes and to gain a general understanding of the said concepts. That being said, I adapted examples as applicable to use my own chosen values or extra additions, but credit for the specific code or processes still goes to the respecful corresponding authors and/or original creators of the content or concepts. 

The sections in the file `notes.md` labeled as "Symmetric vs Asymmetric Encryption", "Caesar Cipher", and "RSA Encryption" contains my progress and notes obtained while following the RealPython [A Brief Introduction to Cryptography](https://realpython.com/lessons/brief-intro-cryptography/) and [Exchanging Asymmetric Keys](https://realpython.com/lessons/asymmetric-keys/) courses by Christopher Trudeau. 

My additions: I created my own examples using different chosen values for the Caesar cipher and RSA Encryption section and paraphrased general information as applicable.

The section in the file `notes.md` labeled as "HMAC" uses an example hash idea adapted from a StackOverflow post called [How to do 8 bit modulo 256 to obtain checksum?](https://stackoverflow.com/questions/49825888/how-to-do-8-bit-modulo-256-to-obtain-checksum) as well as notes obtained from following the tutorial called [How HMAC Works, Step-by-Step Explanation with Examples](https://medium.com/@short_sparrow/how-hmac-works-step-by-step-explanation-with-examples-f4aff5efb40e) by Oleksandr Volkov on Medium. 

My additions: I utilized the idea of 8 bit modulo 256 to create my example hash and created my own example HMAC that differs from the one presented by Volkov, following the general logic and process outlined there. 

The section in the file `notes.md` labeled as "AES Encryption" contains my notes obtained from following the GeeksforGeeks article [Advanced Encryption Standard (AES)](https://www.geeksforgeeks.org/computer-networks/advanced-encryption-standard-aes/). The specific matrices described in the notes were obtained directly from GeeksforGeeks.

My additions: I altered the names of values used in the specific multiplication matrices and paraphrased general information as applicable. 