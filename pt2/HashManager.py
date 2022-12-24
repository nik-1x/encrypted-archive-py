import hashlib
from cryptography.fernet import Fernet
from base64 import b64encode as b64e

class Hash:

    def __init__(self, key):
        self.key = Fernet(
            b64e(
                hashlib.md5(
                    hashlib.sha3_512(key.encode('utf-8')).hexdigest().encode('utf-8')
                    +
                    hashlib.md5(key.encode('utf-8')).hexdigest().encode('utf-8')
                ).hexdigest().encode('utf-8')
            )
        )

    def encrypt(self, data):
        return self.key.encrypt(data)

    def decrypt(self, data):
        return self.key.decrypt(data)