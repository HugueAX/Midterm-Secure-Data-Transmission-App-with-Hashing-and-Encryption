from cryptography.fernet import Fernet
import hashlib

# Convert message to hash
def hash_message(user_string):
    return hashlib.sha256(user_string.encode('utf-8')).hexdigest()

# Encrpt message
def encrypt_message(message):
    # Generate key
    key = Fernet.generate_key()

    # Initialize key
    cipher = Fernet(key)

    # Encrypt message
    message_bytes = message.encode("utf-8")
    cipher_text = cipher.encrypt(message_bytes)
    return cipher, cipher_text

# Decrypt message
def decrypt_message(encrypted_message, cipher):
    # Decrypt the message
    decrypted_bytes = cipher.decrypt(encrypted_message)
    decrypted_message = decrypted_bytes.decode('utf-8')
    return decrypted_message

def compare_hashes(hashed_message, decrypted_hashed_message):
    if (hashed_message == hashed_decrypted_message):
        print("\n[SUCCESS] Message security verified by hash comparison.")
    else:
        print("\n[ERROR] Message failed verification.")

message = input("Enter message to encrypt: ")
hashed_message = hash_message(message)
cipher, encrypted_message = encrypt_message(message)
decrypted_message = decrypt_message(encrypted_message, cipher)
hashed_decrypted_message = hash_message(decrypted_message)
compare_hashes(hashed_message, hashed_decrypted_message)

print(f"\nOriginal Message:          {message}")
print(f"\nOriginal Hash:             {hashed_message}")
print(f"\nEncrypted Message:         {encrypted_message}")
print(f"\nDecrypted Message:         {decrypted_message}")
print(f"\nDecryted Hash:             {hashed_decrypted_message}")
