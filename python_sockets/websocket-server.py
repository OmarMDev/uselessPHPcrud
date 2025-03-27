import asyncio
import websockets
import ssl
import pathlib

async def handle_connection(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            response = input("Enter response to send to client: ")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

start_server = websockets.serve(
    handle_connection, 
    "0.0.0.0", 
    8765, 
    ssl=ssl_context
)

print("WebSocket SSL server started. Waiting for connections...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
