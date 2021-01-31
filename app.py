from fastapi import FastAPI
import os
from routers import users,ads


app = FastAPI()
app.include_router(users.router,prefix='/user')
app.include_router(ads.router,prefix='/ads')
