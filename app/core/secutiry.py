from typing import Hashable
from bcrypt import hashpw, gensalt, checkpw

def create_hash_password(password: str) -> Hashable:
    password = password.encode("utf-8")
    salt = gensalt()
    hashed = hashpw(password, salt)
    return hashed.decode("utf-8")

def check_password(password_hash: str, plain_password: str) -> bool:
    return checkpw(plain_password.encode("utf-8"), password_hash.encode("utf-8"))