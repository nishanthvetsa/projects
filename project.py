from PIL import Image
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_ecc_key():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_data(private_key, data):
    signature = private_key.sign(
        data,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, signature, data):
    try:
        public_key.verify(
            signature,
            data,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False

def encrypt_aes(data, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'1234567890123456'), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return encrypted_data

def encrypt_image(input_image_path, output_image_path):
    # Key Generation for ECC
    private_key_sender, public_key_sender = generate_ecc_key()

    # Image Pixel Processing
    original_image = Image.open(input_image_path)
    pixels = list(original_image.getdata())
    encrypted_pixels = [(pixel[0] + 1, pixel[1] + 2, pixel[2] + 1) for pixel in pixels]
    pixel_bytes = bytes([(pixel_value % 256) for pixel in encrypted_pixels for pixel_value in pixel])

    # ECC Key Exchange
    private_key_receiver, public_key_receiver = generate_ecc_key()  # Receiver generates their key

    # Serialize and deserialize public key using DER format
    public_key_sender_bytes = public_key_sender.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    received_public_key = serialization.load_der_public_key(public_key_sender_bytes, backend=default_backend())

    # Perform ECDH key exchange
    shared_secret = private_key_receiver.exchange(ec.ECDH(), received_public_key)

    # AES Encryption
    encrypted_data = encrypt_aes(pixel_bytes, shared_secret)

    # Save Encrypted Image
    combined_data = public_key_sender.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ) + encrypted_data

    encrypted_image = Image.frombytes('RGB', original_image.size, combined_data)
    encrypted_image.save(output_image_path)

# Example usage:
encrypt_image("C:\\Users\\Nishanth Vetsa\\OneDrive\\Desktop\\IMG_20230918_005257_865.jpg", 'C:\\Users\\Nishanth Vetsa\\OneDrive\\Desktop\\encrypted_image.jpg')
