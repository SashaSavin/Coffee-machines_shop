from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/items/{item_id}/ws")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q":  r1}