import hashlib

class SecurityManager:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.username == username and self.password == hashed_password:
            return True
        else:
            return False
    
    def encrypt(self, data):
        # Реализация метода шифрования данных, например, с помощью AES или RSA
        encrypted_data = data + " encrypted"
        return encrypted_data
