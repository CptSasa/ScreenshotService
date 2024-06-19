from typing import Union
from screenshot import take_screenshot
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/image/{image_name}")
def get_image(image_name: str):
    return FileResponse(screenshot.take_screenshot(image_name))