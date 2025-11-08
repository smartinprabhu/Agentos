from fastapi import APIRouter, WebSocket
from app.llm.client import get_chat_completion
from app.llm.streaming import stream_handler

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = get_chat_completion(data)
        async for chunk in stream_handler(response):
            await websocket.send_text(chunk)
