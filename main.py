from typing import Union
from screenshot import Screenhshot
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/image/{url:path}")
def get_image(url: str):
    try:
        file_path = Screenhshot.take_screenshot(url)
        return FileResponse(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))