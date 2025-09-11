from fastapi import WebSocket

connections = {}


class ConnectionManager:
    @staticmethod
    async def connect(websocket: WebSocket, channel: str):
        await websocket.accept()
        if channel not in connections:
            connections[channel] = []
        connections[channel].append(websocket)

    @staticmethod
    async def disconnect(websocket: WebSocket, channel: str):
        if channel in connections:
            connections[channel].remove(websocket)

    @staticmethod
    async def send_to_channel(channel: str, message: str):
        if channel in connections:
            for ws in connections[channel]:
                try:
                    await ws.send_text(message)
                except:
                    connections[channel].remove(ws)


manager = ConnectionManager()