
from fastapi import APIRouter,UploadFile,File, status, Form
from fastapi.responses import FileResponse, JSONResponse
from app.utils.settings import settings
import os 
from shutil import rmtree

router = APIRouter()

@router.post("/")
async def upload_file(file:UploadFile = File(...)):
    file_path = os.path.join(settings.STORAGE_PATH,file.filename)
    with open(file_path,"wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
        
    return "ok"


@router.get("/{name_file}")
def get_file(
    name_file:str
):
    # Posiblemente tener instalado aiofiles
    return FileResponse(
        os.path.join(settings.STORAGE_PATH,name_file)
    )


@router.get("/download/{name_file}")
def get_file(
    name_file:str
):
    # Posiblemente tener instalado aiofiles
    return FileResponse(
        os.path.join(settings.STORAGE_PATH,name_file),
        media_type="application/octet-stream",
        filename=name_file
    )



@router.delete("/delete/{name_file}")
def get_file(
    name_file:str
):
    try:
        os.remove(os.path.join(settings.STORAGE_PATH,name_file))
    except FileNotFoundError as e:
        return JSONResponse(
            content={
                "removed":False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "msg":str(e)
            }
        )
    return JSONResponse(
    content={
        "removed":True,
        "status_code": status.HTTP_200_OK,
        "msg":f"{name_file} removed"
    }
)


@router.delete("/deletefolder")
def get_file(
    folder_name:str = Form(...)
):
    try:
        rmtree(os.path.join(settings.STORAGE_PATH,folder_name))
    except FileNotFoundError as e:
        return JSONResponse(
            content={
                "removed":False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "msg":str(e)
            }
        )
    return JSONResponse(
    content={
        "removed":True,
        "status_code": status.HTTP_200_OK,
        "msg":f"{folder_name} removed"
    }
)