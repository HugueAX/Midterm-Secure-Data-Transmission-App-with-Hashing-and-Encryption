# Midterm-Secure-Data-Transmission-App-with-Hashing-and-Encryption
This script prompts the user to input a message and contains functions to symmetrically encrypt and decrypt it. It hashes the input using SHA-256 and encrypts it using symmetric encryption.  After decrypting the encrypted message is hashes the decrypted message.  It then compares the original message's hash to the decrypted message's hash in order to verify the integrity of the security measures.

This script currently focuses on the Integrity aspect of the CIA triad by checking for modifications to the original message. By comparing the hashes from the original message and the encrypted message it verifies that the message was not tampered with during the process. Hash comparison ensures that the information remains accurate and trustworthy.

Entropy is paramount to secure key generation during the encryption process.  High entropy and randomness makes it less likely for keys to be guessed or broken.
