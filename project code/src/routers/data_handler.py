from fastapi import APIRouter,UploadFile,file,HTTPException,Query

import uuid as uuid_pkg # Use alies to avoid conflicts with path parameter name

import os

# import the share data stored

from src.data_store import data_store

# Pdf processing utility functions
from src.utils.pdf_processor import extract_text_from_pdf

# llm client utility 
from src.utils.llm_client import get_llm_responce, get_llm_response

router = APIRouter()

# define temporary dictionary for upload
UPLOAD_DIR="/tmp/cag_uploads"

os.makedirs(UPLOAD_DIR,exist_ok=True)
@router.post("/upload/{uuid}",status_code=201)

def upload_pdf(uuid:uuid_pkg.UUID,file:UploadFile=file(...)):
    """
    Upload a PDF file associated with a specific UUID.
    extract text from the pdf and store in in the data store
    if the uuid already exists, it raises an error (useput to update)
    """
    # Check if the uploaded file is a PDF
    
    if file.content_type != "application/pdf":

        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    uuid_str = str(uuid)
    if uuid_str in data_store:
        raise HTTPException(status_code=400, detail=f"UUID {uuid_str} already exists. Use PUT/api/v1/update/{uuid_str}to append the existing entry."
        )
    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")
    try:
        # Save the uploaded file to the temporary directory
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(file_path)
        if extracted_text is None:
            raise HTTPException(status_code=500, detail="Failed to extract text from the PDF.")
        # Store the extracted text in the data store
        data_store[uuid_str] = extracted_text
        return{
            "message": f"File uploaded and text extracted successfully", "uuid": uuid_str,
        }
    except Exception as e:
        # log the exception e
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}",)
    finally:
        # clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
@router.put("/update/{uuid}")
def update_pdf_data(uuid:uuid_pkg.UUID,file:UploadFile=file(...)):
    """
    append text extracted from a new pdf file to the existing data for a specific UUID in the data store.
    if the uuid does not exist, its raises an error.
    """
    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail=f"UUID {uuid_str} not found. Use POST/api/v1/upload/{uuid_str} to create a new entry.")
    
    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")
    try:
        # Save the uploaded file to the temporary directory
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        
        # Extract text from the PDF
        new_text = extract_text_from_pdf(file_path)
        if new_text is None:
            raise HTTPException(status_code=500, detail="Failed to extract text from the PDF.")
        
        # Append the extracted text to the existing entry in the data store
        data_store[uuid_str] += "\n" + new_text
        
        return {
            "message": f"data appended successfully", "uuid": uuid_str,
        }
    except Exception as e:
        # log the exception e
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}",)
    finally:
        # clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
@router.get("/query/{uuid}")
def query_pdf_data(uuid:uuid_pkg.UUID,query:str=Query(...,min_length=1)):
    """
    retrieve the stored text for a given uuid and send it along with a 
    query to a place holder LLM service.
    return the place holder responce.
    """
    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail=f"UUID {uuid_str} not found.")
    
    # Retrieve the extracted text from the data store
    stored_text = data_store[uuid_str]
    
    # Use the LLM client to get a response based on the query and extracted text
    llm_response = get_llm_response(context=stored_text, query=query)
    
    return {
        "uuid": uuid_str,
        "query": query,
        "llm_response": llm_response,
    }
@router.delete("/delete/{uuid}")
def delete_data(uuid:uuid_pkg.UUID):
    """
    delete the data associated with a specific uuid from the data store.
    """
    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail=f"UUID {uuid_str} not found.")
    
    # Remove the entry from the data store
    del data_store[uuid_str]
    
    return {
        "message": f"Data for UUID {uuid_str} deleted successfully.",
        "uuid": uuid_str,
    }