# ECC Certificate Parameter Extractor

This Python utility extracts Elliptic Curve Cryptography (ECC) parameters—specifically the curve equation and finite field characteristic—from a PEM-encoded X.509 certificate.

It parses the ASN.1 structure of the certificate to identify the public key curve (e.g., `secp256r1`) and outputs the underlying mathematical properties used for the cryptography.

## 📂 Project Structure

* `main.py`: The core script that parses the certificate and prints the parameters.
* `cert.pem`: The target certificate file (input).
* `requirements.txt`: List of Python dependencies.

## 🚀 Setup & Usage

### 1. Install Dependencies
Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt