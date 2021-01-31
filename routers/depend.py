import os
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from dotenv import load_dotenv

from db.user import User
usr = User()


load_dotenv()

auth_scheme = HTTPBearer()


def get_current_user(auth: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        token = auth.credentials
        payload = jwt.decode(token, os.getenv(
            'JWT_SECRET'), os.getenv('JWT_ALGORITHM'))
        id = payload.get('id')
        user = usr.get_user_by_id(id)
        if user is None:
            raise credentials_exception
        return user
    except:
        raise credentials_exception
