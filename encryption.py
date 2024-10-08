from cryptography.fernet import Fernet

# Générer la key de chiffrement
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Chiffrement du texte
def encrypt_message(message):
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text

# Déchiffrement du texte
def decrypt_message(cipher_text):
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

if __name__ == '__main__':
    message = "ATTENTION ! Données sensibles"
    encrypted_message = encrypt_message(message)
    print(f"Message chiffré : {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message)
    print(f"Message déchiffré : {decrypted_message}")
