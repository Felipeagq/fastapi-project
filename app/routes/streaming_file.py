
from fastapi import APIRouter, Header
import os
from fastapi.responses import Response
from app.utils.settings import settings

router = APIRouter()

PORTION_SIZE = 1024 * 1024

@router.get("/{name_video}")
def get_video(
    name_video:str,
    range:str = Header(None)
):
    start,end = range.replace("bytes=","").split("-")
    start = int(start)
    end = int(start + PORTION_SIZE)
    file_path = os.path.join(settings.STORAGE_PATH,name_video)
    with open(file_path,"rb") as myfile:
        myfile.seek(start)
        data = myfile.read(end - start)
        size_video = str(os.path.getsize(file_path))
        headers = {
            "Content-Range": f"bytes {str(start)}-{str(end)}/{size_video}",
            "Accept-Ranges": "bytes"
        }
        return Response(
            content=data,
            status_code=206,
            headers=headers,
            media_type="video/mp4"
        )