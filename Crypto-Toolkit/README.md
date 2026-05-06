# Crypto Toolkit CLI

## Purpose

This project demonstrates RSA and AES encryption with HMAC verification in a Python CLI.

## Features

- Generate RSA key pair
- Encrypt and decrypt messages with hybrid AES-RSA encryption
    - Message is encrypted with AES while the AES key is encrypted with RSA public key
    - Message is decrypted with AES while the AES key is decrypted with RSA private key
- Verify message integrity with HMAC
- Command-line interface (argparse)

## How to Run

1. Install requirements (inside of project directory, this is important): `pip install -r requirements.txt`
    - Create a virtual environment inside of your project directory: `python3 -m venv <venv_name>`
2. Activate virtual environment (replace `<venv_name>` with name of your virtual environment): `source <venv_name>/bin/activate`
3. Run CLI: `python3 crypto_toolkit.py`
4. Follow prompts to encrypt/decrypt messages
5. Deactivate virtual environment when done: `deactivate`

## Usage

1. Generate keys:

    ```bash
    python3 crypto_toolkit.py --generate-keys
    ```

2. Encrypt message:

    ```bash
    python3 crypto_toolkit.py --encrypt "Hello world!"
    ```

3. Decrypt message:

    ```bash
    python3 crypto_toolkit.py --decrypt <encrypted_json_file_name>
    ```

## Tools

- Python3

- PyCryptodome

- argparse

## Diagrams

## Screenshots

## Learning Outcomes

- Applied cryptogoraphy concepts (RSA, AES, HMAC)
- Built a secure CLI application
- Learned project documentation and workflow diagrams

## Run Unit Tests

1. Install requirements (inside of project directory, this is important): `pip install -r requirements.txt`
    - Create a virtual environment inside of your project directory: `python3 -m venv <venv_name>`
2. Activate virtual environment (replace `<venv_name>` with name of your virtual environment): `source <venv_name>/bin/activate`
3. Run: `python3 -m unittest tests.py` or `python3 -m unittest -v tests.py`
4. Deactivate virtual environment when done: `deactivate`