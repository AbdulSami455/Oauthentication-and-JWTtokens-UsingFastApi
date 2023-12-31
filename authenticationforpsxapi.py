from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import  CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel
#from otherdata.data import volume,status,companiesinloss,companiesinprofit,totalcompanies,trades
#from sectorwise.sectors import somesector,numberofshare,indicesshare,sectorsshare
#from indices.getcompanydata import companydata,getcompanyprofile,equityprofile

#secretkey,algorithm and Access_token_expire for api
SECRET_KEY = "27437940fd78c03104d9ab1d38095d187a96cf8aeeb1f5d74dde00afe6aa423f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


#Pydantic Models for Different WOrks
class User(BaseModel):
    username: str
    password: str



#model for token
class Token(BaseModel):
    access_token: str
    token_type: str


#WE create own database in Progrma for authentication
fake_users_db = {}

new_username = "abdulsami"
new_password = "1234"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#function to verify password from hashing done on it
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


#get hash password
def get_password_hash(password):
    return pwd_context.hash(password)

fake_users_db[new_username] = {
    "username": new_username,
    "hashed_password": get_password_hash(new_password),
}

#function to authenticate user from database
def authenticate_user(username: str, password: str):
    if username in fake_users_db:
        user = fake_users_db[username]
        if verify_password(password, user["hashed_password"]):
            return user

    return None

#function to create access token for authentication
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


#intilize fastapi to create api
app = FastAPI()


#first post request to get token
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


#get request to find token is correct or not
@app.get("/protected")
async def protected_route(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return {"message": "You are authenticated!"}

