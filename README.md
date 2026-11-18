# ChaCha20-Poly1305 Security Lab

A practical implementation of the **ChaCha20-Poly1305** authenticated encryption algorithm using Python and the `cryptography` library.

This project was developed for the **Information Security** course to demonstrate secure encryption, decryption, data integrity, and authentication.

## Features

- **Encryption:** Encrypts confidential messages using ChaCha20-Poly1305.
- **Decryption:** Recovers the original message using the correct key and nonce.
- **Integrity Verification:** Detects modifications to encrypted data.
- **AAD Validation:** Tests authentication using Additional Authenticated Data (AAD).
- **Nonce Validation:** Demonstrates how an incorrect nonce causes authentication failure.
- **Interactive Menu:** Provides a simple terminal interface to execute the demonstrations.

## Technologies

- Python 3
- ChaCha20-Poly1305
- Cryptography Library

## Requirements

- Python 3.8+
- cryptography

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/chacha20-poly1305-security-lab.git
cd chacha20-poly1305-security-lab
```

Install the required dependency:

```bash
pip install cryptography
```

## Usage

Run the program:

```bash
python3 main.py
```

The interactive menu provides two options:

1. **Normal Execution:** Demonstrates message encryption and decryption.
2. **Security Tests:** Performs tests involving:
   - Modification of encrypted data.
   - Alteration of Additional Authenticated Data (AAD).
   - Use of an incorrect nonce.

## Security Concepts

This project demonstrates important concepts in information security:

- **Confidentiality:** Protects information through encryption.
- **Integrity:** Detects unauthorized modifications to encrypted messages.
- **Authentication:** Verifies that encrypted data and associated information have not been altered.
- **AEAD:** Authenticated Encryption with Associated Data.

## Academic Context

Developed as a practical exercise for the **Information Security** course, focusing on authenticated encryption and the verification of data integrity.

---

**Note:** This project is intended for educational purposes and cryptographic experimentation.
