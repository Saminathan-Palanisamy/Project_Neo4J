import os, shutil, uuid
from fastapi import APIRouter, UploadFile, File
from original_processor import store_original
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/original")
def ingest_original(file: UploadFile = File(...)):
    try:
        path = f"uploads/original/{file.filename}"
        os.makedirs("uploads/original", exist_ok=True)

        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        doc_id = store_original(path)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "stored", "doc_id": doc_id})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"unable to process: {str(e)}")

