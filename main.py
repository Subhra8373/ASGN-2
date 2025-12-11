import sys
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

def extract_curve_info(file_path):
    try:
        with open(file_path, 'rb') as f:
            pem_data = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{file_path}'")
        return

    # Load the certificate
    try:
        cert = x509.load_pem_x509_certificate(pem_data, default_backend())
    except ValueError:
        print("Error: Invalid PEM format.")
        return

    public_key = cert.public_key()

    if isinstance(public_key, ec.EllipticCurvePublicKey):
        curve = public_key.curve
        key_size = public_key.key_size
        
        print("=== Elliptic Curve Details ===")
        print(f"Curve Name: {curve.name}")
        print(f"Key Size:   {key_size} bits")
        
        # Standard SECP256R1 Parameters (NIST P-256)
        # These are constant for this curve name
        if curve.name == 'secp256r1':
            p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
            b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
            
            print("\n=== Mathematical Parameters (Finite Field) ===")
            print(f"Field Characteristic (p): \n{p}")
            print(f"\nEquation Structure:")
            print(f"y^2 = x^3 - 3x + {hex(b)} (mod p)")
        else:
            print(f"\nNote: Standard parameters for {curve.name} are defined in SECG standards.")
            
    else:
        print("The certificate does not use Elliptic Curve Cryptography (ECC).")

if __name__ == "__main__":
    # Checks if a filename was provided, otherwise defaults to cert.pem
    filename = sys.argv[1] if len(sys.argv) > 1 else "cert.pem"
    extract_curve_info(filename)