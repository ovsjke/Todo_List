from bcrypt import hashpw, gensalt, checkpw
from typing import Annotated
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import UUID
import jwt

type JWTstring = Annotated(str,"JWT Token") # type: ignore

def create_hash_password(password: str) -> str:
    password = password.encode("utf-8")
    salt = gensalt()
    hashed = hashpw(password, salt)
    return hashed.decode("utf-8")

def check_password(password_hash: str, plain_password: str) -> bool:
    return checkpw(plain_password.encode("utf-8"), password_hash.encode("utf-8"))

PRIVATE_KEY = Path("app/certs/private_key.pem").read_text()
PUBLIC_KEY = Path("app/certs/public_key.pem").read_text()
ALGORITHM = "RS256"


def jwt_encode(id: UUID) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(id),
        "exp": now+timedelta(minutes=30),
        "iat": now
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm = ALGORITHM)

def jwt_decode(token: JWTstring):
    try:
        data = jwt.decode(token, PUBLIC_KEY, algorithms= [ALGORITHM])
        return data
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    