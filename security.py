from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def authenticate(token):
    return token == "FOG_SECURE_123"

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()
