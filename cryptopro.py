from PIL import Image
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Function to generate ECC private and public key pair
def generate_ecc_key():
    # Generate a private key for ECC using the SECP256R1 curve and the default backend
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    
    # Derive the corresponding public key from the private key
    public_key = private_key.public_key()
    
    # Return both private and public keys
    return private_key, public_key

# Function to sign some data using a private key
def sign_data(private_key, data):
    # Use the private key to sign the data using the ECDSA (Elliptic Curve Digital Signature Algorithm) with SHA-256 hashing
    signature = private_key.sign(
        data,
        ec.ECDSA(hashes.SHA256())
    )
    
    # Return the signature generated
    return signature

# Function to verify a signature using a public key
def verify_signature(public_key, signature, data):
    try:
        # Try to verify the signature using the public key and ECDSA with SHA-256
        public_key.verify(
            signature,
            data,
            ec.ECDSA(hashes.SHA256())
        )
        # If verification succeeds, return True
        return True
    except:
        # If verification fails (throws exception), return False
        return False

# Function to perform AES encryption on data
def encrypt_aes(data, key):
    # Create an AES cipher object using CFB mode with an initialization vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'1234567890123456'), backend=default_backend())
    
    # Create an encryptor object from the cipher to perform the encryption
    encryptor = cipher.encryptor()
    
    # Perform the encryption and finalize it
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    
    # Return the encrypted data
    return encrypted_data

# Function to process and encrypt the image data
def process_image_data(image):
    # Retrieve the pixel data from the image
    pixels = list(image.getdata())
    
    # Perform a simple encryption-like transformation on the pixel data by altering each channel slightly
    encrypted_pixels = [(pixel[0] + 1, pixel[1] + 2, pixel[2] + 1) for pixel in pixels]
    
    # Convert the pixel data into a flat list of byte values, ensuring all values remain within 0-255
    pixel_bytes = bytes([(pixel_value % 256) for pixel in encrypted_pixels for pixel_value in pixel])
    
    # Return the processed pixel bytes
    return pixel_bytes

# Function to perform ECC key exchange and derive a shared secret
def perform_key_exchange(private_key, public_key_bytes):
    # Deserialize the public key bytes into a public key object
    peer_public_key = ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256R1(), public_key_bytes
    )
    
    # Perform the key exchange to derive the shared secret using ECDH (Elliptic Curve Diffie-Hellman)
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
    
    # Return the shared secret
    return shared_secret

# Function to encrypt the image using ECC key exchange and AES encryption
def encrypt_image(input_image_path, output_image_path):
    # Step 1: Generate ECC key pair for the sender
    print("Generating ECC key for the sender...")
    private_key_sender, public_key_sender = generate_ecc_key()

    # Step 2: Open and process the input image
    print(f"Loading image from {input_image_path} and processing its pixels...")
    original_image = Image.open(input_image_path)
    pixel_bytes = process_image_data(original_image)

    # Step 3: Generate ECC key pair for the receiver (simulating key exchange scenario)
    print("Generating ECC key for the receiver...")
    private_key_receiver, public_key_receiver = generate_ecc_key()

    # Step 4: Perform ECC key exchange to derive shared secret
    print("Performing key exchange to derive the shared secret...")
    public_key_bytes_receiver = public_key_receiver.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    shared_secret = perform_key_exchange(private_key_sender, public_key_bytes_receiver)
    
    # Step 5: AES encryption of the pixel data using the shared secret
    print("Encrypting image data using AES encryption with the shared secret...")
    aes_key = shared_secret[:32]  # Use the first 32 bytes of shared secret as AES key
    encrypted_data = encrypt_aes(pixel_bytes, aes_key)

    # Step 6: Combine public key and encrypted image data
    print("Combining sender's public key and encrypted image data...")
    combined_data = public_key_sender.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    ) + encrypted_data

    # Step 7: Create and save the encrypted image
    print(f"Saving the encrypted image to {output_image_path}...")
    encrypted_image = Image.frombytes('RGB', original_image.size, combined_data[:len(pixel_bytes)])
    encrypted_image.save(output_image_path)

    print("Encryption process completed successfully.")

# Example usage
encrypt_image(r"C:\Users\Nishanth Vetsa\OneDrive\Desktop\WhatsApp.jpg", 
              r'C:\Users\Nishanth Vetsa\OneDrive\Desktop\WhatsApp Image 2023-09-09 at 12.05.21.jpg')
