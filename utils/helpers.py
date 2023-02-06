import uuid
import hashlib


class Helpers:
    
    @staticmethod
    def create_hash_id():

        id = uuid.uuid4()

        return str(id)

    @staticmethod
    def md5_password(password):
        
        convert_password = password.encode('ascii')
        md5_password = hashlib.md5(convert_password).hexdigest()

        return md5_password
