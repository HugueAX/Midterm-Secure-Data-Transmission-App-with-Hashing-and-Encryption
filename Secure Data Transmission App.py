from cryptography.fernet import Fernet
import hashlib

# convert user string to hash
def hash_string(user_string):
    return hashlib.sha256(user_string.encode('utf-8')).hexdigest()
    

def encryptHash(hashed_message):
    # Generate key
    key = Fernet.generate_key()

    # Initialize key
    cipher = Fernet(key)

    # Encrypt message
    message_bytes = hashed_message.encode("utf-8")
    cipher_text = cipher.encrypt(message_bytes)
    # Return cipher and encrypted text
    return cipher, cipher_text

def decryptHash(encrypted_hashed_message, cipher):
    # Decrypt the message
    decrypted_bytes = cipher.decrypt(encrypted_hashed_message)
    decrypted_message = decrypted_bytes.decode('utf-8')
    return decrypted_message

def compareHashes(hashed_message, decrypted_hashed_message):
    if (hashed_message == decrypted_hashed_message):
        print("\n[SUCCESS] Message security verified by hash comparison.")
    else:
        print("\n[ERROR] Message failed verification.")

message = input("Enter message to encrypt: ")
hashed_message = hash_string(message)
cipher, encrypted_hashed_message = encryptHash(hashed_message)
decrypted_hashed_message = decryptHash(encrypted_hashed_message, cipher)
compareHashes(hashed_message, decrypted_hashed_message)

print(f"Original Message:          {message}")
print(f"Original Hash:             {hashed_message}")
print(f"Encrypted Hash:    {encrypted_hashed_message}")
print(f"Decrypted Hash:            {decrypted_hashed_message}")
