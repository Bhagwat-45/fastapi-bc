from datetime import timedelta,datetime
from passlib.context import CryptContext
import jwt
from src.config import Config
import uuid
import logging 


password_context = CryptContext(
    schemes=[
        'bcrypt'
    ]
)

def generate_password_hash(
        password: str
) -> str:
    hash = password_context.hash(password)
    return hash

def verify_password_hash(
        password: str, hash: str
) -> bool:
    return password_context.verify(password,hash)


def create_passcode(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = {

    }

    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=Config.ACCESS_TOKEN_EXPIRY))
    payload['jti'] = str(uuid.uuid4())

    token = jwt.encode(
    payload=payload,
    key=Config.JWT_SECRET,
    algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> str:
    try:
        token = jwt.decode(
            jwt=token,
            algorithms=Config.JWT_ALGORITHM,
            key=Config.JWT_SECRET
        )
        return token
    except jwt.PyJWTError as e:
        logging.exception(e)
        return e 