import unittest
import os
import json
from crypto_toolkit import (
    aes_encrypt, aes_decrypt, generate_RSA_keys,
    encrypt, decrypt
)

class TestCryptoToolkit(unittest.TestCase):

    def test_aes_encryption_and_decryption(self):
        plaintext = "hello"
        key, nonce, ciphertext, tag = aes_encrypt(plaintext)
        decrypted_text = aes_decrypt(key, nonce, ciphertext, tag)

        self.assertEqual(decrypted_text, plaintext)

    def test_modified_ciphertext_tampering(self):
        plaintext = "hello"

        key, nonce, ciphertext, tag = aes_encrypt(plaintext)

        tampered = bytearray(ciphertext)
        tampered[0] ^= 1  # flip a bit

        with self.assertRaises(ValueError):
            aes_decrypt(key, nonce, bytes(tampered), tag)

    def test_incorrect_rsa_key(self):
        generate_RSA_keys()
        encrypt("secret message")

        # change RSA keys
        generate_RSA_keys()

        with self.assertRaises(ValueError):
            decrypt("encrypted_output.json")

    def test_encryption_without_rsa_keys(self):
        if os.path.exists("keys/public.pem"):
            os.remove("keys/public.pem")

        with self.assertRaises(FileNotFoundError):
            encrypt("hello")

    def test_decrypt_missing_file(self):
        with self.assertRaises(ValueError):
            decrypt(None)

    def test_invalid_ciphertext_input(self):
        with open("encrypted_output.json", "r") as f:
            items = json.load(f)

        items["ciphertext"] = "bad text"

        with self.assertRaises((ValueError, json.JSONDecodeError)):
            decrypt("encrypted_output.json")

    def test_missing_encrypt_message(self):
        with self.assertRaises(ValueError):
            encrypt("")

    def test_large_encryption_message(self):
        plaintext = "A" * 1000000  # 1 MB

        key, nonce, ciphertext, tag = aes_encrypt(plaintext)
        decrypted = aes_decrypt(key, nonce, ciphertext, tag)

        self.assertEqual(decrypted, plaintext)

    def test_repeated_encryption(self):
        plaintext = "hello"

        key, nonce, ciphertext, tag = aes_encrypt(plaintext)
        key2, nonce2, ciphertext2, tag2 = aes_encrypt(plaintext)

        self.assertNotEqual(ciphertext, ciphertext2)

    def test_missing_rsa_key_file(self):
        if os.path.exists("keys/private.pem"):
            os.remove("keys/private.pem")

        with self.assertRaises(FileNotFoundError):
            decrypt("encrypted_output.json")

    def test_invalid_decryption_file_input(self):
        with self.assertRaises(FileNotFoundError):
            decrypt("nonexistent.json")

if __name__ == "__main__":
    unittest.main()