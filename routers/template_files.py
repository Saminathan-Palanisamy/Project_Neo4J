import os, shutil, uuid
from fastapi import APIRouter, UploadFile, File

from template_workflow import build_workflow
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/template")
def ingest_template(file: UploadFile = File(...)):
    try:
        path = f"uploads/template/{uuid.uuid4()}_{file.filename}"
        os.makedirs("uploads/template", exist_ok=True)

        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        workflow = build_workflow()
        result = workflow.invoke({"template_path": path})

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
            "status": "success",
            "output": result["output"],
            "resolved": result["resolved"]
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"unable to process: {str(e)}")

