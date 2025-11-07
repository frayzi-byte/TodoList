from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.future import select
from app.db import async_session
from app.models.user_model import NewUser
from app.core.security import SECRET_KEY, ALGORITHM

bearer_scheme = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    async with async_session() as session:
        result = await session.execute(select(NewUser).where(NewUser.email == email))
        user = result.scalars().first()

    if user is None:
        raise credentials_exception

    return user
