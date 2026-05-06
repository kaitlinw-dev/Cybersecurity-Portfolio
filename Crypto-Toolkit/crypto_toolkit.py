import argparse
import os
from Cryptodome.PublicKey import RSA

def rsa_encrypt():
    pass

def rsa_decrypt():
    pass

def aes_encrypt():
    pass

def aes_decrypt():
    pass

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

    print("RSA key pair generated")

def encrypt(plaintext):
    pass

def decrypt(ciphertext):
    pass

def verify(ciphertext, hmac):
    pass

def main():
    parser = argparse.ArgumentParser(description="Crypto Toolkit CLI")

    parser.add_argument('--generate-keys',
                        action='store_true',
                        help='Generate RSA key pair')
    
    parser.add_argument('--encrypt',
                        type=str,
                        metavar='<plaintext_message>',
                        help='Encrypt plaintext message using AES and RSA key wrapping')
    
    parser.add_argument('--decrypt',
                        metavar='<encrypted_text>',
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