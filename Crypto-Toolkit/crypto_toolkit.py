import argparse
import os
import json
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Random import get_random_bytes

def rsa_encrypt(data, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(data)

def rsa_decrypt(data, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(data)

def aes_encrypt(message):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    return key, cipher.nonce, ciphertext, tag

def aes_decrypt(key, nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode()
    cipher.verify(tag)
    return plaintext

def generate_hmac():
    pass

def verify_hmac():
    pass

def generate_RSA_keys():
    key = RSA.generate(2048)

    os.makedirs("keys", exist_ok = True)

    private_key = key.export_key()
    with open ("keys/private.pem", "wb") as f:
        f.write(private_key)

    public_key = key.publickey().export_key()
    with open ("keys/public.pem", "wb") as f:
        f.write(public_key)

    print("RSA key pair generated, see keys/ directory")

def encrypt(plaintext):
    if not os.path.exists("keys/public.pem"):
        raise FileNotFoundError("RSA keys must be generated first")
    
    if not plaintext:
        raise ValueError("Plaintext cannot be empty")

    with open("keys/public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    # encrypt plaintext message with AES
    aes_key, nonce, ciphertext, tag = aes_encrypt(plaintext)

    # encrypt AES session key with public RSA key
    enc_aes_key = rsa_encrypt(aes_key, public_key)

    items = {
        "ciphertext": ciphertext.hex(),
        "nonce": nonce.hex(),
        "encrypted_aes_key": enc_aes_key.hex(),
        "tag": tag.hex()
    }

    with open("encrypted_output.json", "w") as f:
        json.dump(items, f, indent=4)

    print("Encrypted message in filename: encrypted_output.json")

def decrypt(file):
    if not file:
        raise ValueError("Missing input file")
    
    if not os.path.exists(file):
        raise FileNotFoundError("Input file does not exist")
    
    if not os.path.exists("keys/private.pem"):
        raise FileNotFoundError("Private key not found")

    with open("keys/private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    with open(file, "r") as f:
        items = json.load(f)

    try:
        ciphertext = bytes.fromhex(items["ciphertext"])
    except Exception:
        raise ValueError("Invalid ciphertext format")

    nonce = bytes.fromhex(items["nonce"])
    enc_aes_key = bytes.fromhex(items["encrypted_aes_key"])
    tag = bytes.fromhex(items["tag"])

    # decrypt AES session key with private RSA key
    dec_aes_key = rsa_decrypt(enc_aes_key, private_key)

    # decrypt ciphertext message with AES
    plaintext = aes_decrypt(dec_aes_key, nonce, ciphertext, tag)

    print("Message decrypted:\n", plaintext)

def verify(ciphertext, hmac):
    pass

def main():
    parser = argparse.ArgumentParser(description="Crypto Toolkit CLI")

    parser.add_argument('--generate-keys',
                        action='store_true',
                        help='Generate RSA key pair')
    
    parser.add_argument('--encrypt',
                        type=str,
                        metavar='"<plaintext_message>"',
                        help='Encrypt plaintext message using AES and RSA key wrapping')
    
    parser.add_argument('--decrypt',
                        metavar='<encrypted_output_json_file>',
                        help='Decrypt message using RSA and AES')
    
    parser.add_argument('--verify',
                        nargs=2,
                        metavar=('<encrypted_text>','<hmac>'),
                        help='Verify message integrity using HMAC')
    
    args = parser.parse_args()

    if args.generate_keys:
        generate_RSA_keys()

    elif args.encrypt:
        encrypt(args.encrypt)

    elif args.decrypt:
        decrypt(args.decrypt)

    elif args.verify:
        verify(args.verify)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()