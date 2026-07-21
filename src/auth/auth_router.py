from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from .auth_schemas import UserCreate, User, UserLogin
from .services import UserService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .utils import create_passcode, decode_token, verify_password_hash
from datetime import timedelta
from src.config import Config


auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user_account(
    user_data: UserCreate, session: AsyncSession = Depends(get_session)
):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT
        )

    new_user = await user_service.create_user(user_data, session)
    return new_user

@auth_router.post("/login")
async def login_users(login_data: UserLogin, session : AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user(email=email, session=session)

    if user is not None:
        password_valid: bool = verify_password_hash(password, user.password_hash)

        if password_valid:
            access_token = create_passcode(
                user_data={
                    'email' : user.email,
                    'user_uid' : str(user.uid)
                }
            )

            refresh_token = create_passcode(
                user_data={
                    'email' : user.email,
                    'user_id' : str(user.uid)
                },
                refresh=True,
                expiry=timedelta(days=Config.REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content={
                    "message" : "Login Successfull",
                    "access_token" : access_token,
                    "refresh_token" : refresh_token,
                    "user" : {
                        "email" : user.email,
                        "uid" : str(user.uid)
                    }
                }
            )
        

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid Email or Password"
    )