from cryptography.fernet import Fernet

class Crypto:

    def __init__(self, key):
        self.key = key

    def generate_key(self):
        """
        Generate a random encryption key.
        """
        return Fernet.generate_key()

    def encrypt(self, plaintext):
        """
        Encrypt plaintext data with a given key.
        Args:
            key (bytes): The encryption key.
            plaintext (str): The data to be encrypted.
        Returns:
            bytes: The encrypted data.
        """
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(bytes(plaintext, 'utf-8'))
        return encrypted_data

    def decrypt(self, encrypted_data):
        """
        Decrypt encrypted data with a given key.
        Args:
            key (bytes): The decryption key.
            encrypted_data (bytes): The data to be decrypted.
        Returns:
            str: The decrypted data as a string.
        """
        cipher_suite = Fernet(self.key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')
