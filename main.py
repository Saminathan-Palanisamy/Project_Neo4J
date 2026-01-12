from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers import original_files
from routers import template_files

app = FastAPI(title="Project_Neo4j_LangGraph")


app.include_router(original_files.router, prefix="/original",tags=["Original Ingest"])

app.include_router(template_files.router, prefix="/template",tags=["Template Workflow"])

@app.get("/")
def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Neo4j + LangGraph project running ",
            "note": "Original ingest & Template workflow ready"
        }
    )
