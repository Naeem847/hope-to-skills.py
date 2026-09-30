from fastapi import APIRouter,UploadFile,file,HTTPException,Query
import uuid as uuid_pkg # Use alies to avoid conflicts with path parameter name
import os
# import the share data stored
from src.data_store import data_store


router = APIRouter()