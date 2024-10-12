from cryptography.fernet import Fernet
import hashlib
import base64


def getKey(string):
    hash_object = hashlib.sha256(string.encode('utf-8'))
    hashed_string = hash_object.digest()
    key = hashed_string[:32]
    crypt_key = base64.urlsafe_b64encode(key)
    return crypt_key

class crypt:

    def __init__(self, key = bytes):
        self.crypt_key = key

    def Decrypt(self, encryptedText):
        f = Fernet(self.crypt_key)
        decrypted_message = f.decrypt(encryptedText.encode())
        return decrypted_message.decode() 

    def Encrypt(self, Text):
        f = Fernet(self.crypt_key)
        encrypted_message = f.encrypt(Text.encode())
        return encrypted_message.decode()
    
    
