from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .utils import generate_password_hash
from .auth_schemas import UserCreate
from fastapi import HTTPException, status


class UserService:

    async def get_user(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        user = result.first()
        return user

    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user(email, session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreate, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.password_hash = generate_password_hash(user_data_dict["password"])

        session.add(new_user)

        await session.commit()

        return new_user
