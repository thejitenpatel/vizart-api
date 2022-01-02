from fastapi import status, HTTPException, APIRouter
from fastapi.param_functions import Form
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_400_BAD_REQUEST
from ..database import get_db
from .. import models, schemas, utils
import uuid


router = APIRouter(
    prefix="/user",
    tags=["Register"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    if(len(str(user.number)) < 10):
        print("[INFO] inside number")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail=f"Kidnly send a valid data")
    new_user = models.Users(id=str(uuid.uuid1()), **user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}")
async def get_user(id: str, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} doesn't exist!")
    return user
