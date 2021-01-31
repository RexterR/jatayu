import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError
from db.user import User
from db.employee import Employee
from routers.depend import get_current_user
router = APIRouter()
load_dotenv()
empl = Employee()


class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserCredential(BaseModel):
    email: EmailStr
    password: str


usr = User()
pwd_context = CryptContext(schemes=['bcrypt'])


def create_token(data: dict, expires_delta: Optional[timedelta] = None):
    """ Create any token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow()+timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv(
        'JWT_SECRET'), algorithm="HS256")
    return encoded_jwt


def hash_password(pwd: str):
    return pwd_context.hash(pwd)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(user: UserCredential):
    """Authenticating the users"""
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        userDetail = usr.get_user_by_email(user.email)
        if not userDetail:
            raise exception
        pwd = userDetail['password']
        if not verify_password(user.password, pwd):
            raise exception
        return userDetail
    except Exception:
        raise exception


@router.post("/register")
async def register_user(user: RegisterUser):
    try:
        isUser = usr.get_user_by_email(user.email)
        if isUser:
            raise Exception("User already Exists")
        user = dict(user)
        user.update({"password": hash_password(user["password"])})
        result = usr.insert_user(user)
        inserted_id = str(result.inserted_id)
        return {'Sucess': True, 'Result': {'id': inserted_id}}
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


@router.post("/login")
async def login_user(userBody: UserCredential):
    try:
        user = authenticate_user(userBody)
        data = {"id": str(
            user["_id"]), "role": user["role"]}
        access_token = create_token(data)
        return {"success": True, "access_token": access_token}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)



@router.get('/employee')
def return_all_employee(user=Depends(get_current_user)):
    try:
        List = []
        employees = empl.getAll()
        for employee in employees:
            List.append(str(employee['_id']))
        return List
    except Exception as e:
        raise HTTPException(status_code=500)
