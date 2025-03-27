import asyncio
import websockets
import ssl

async def handle_connection(websocket, path=None):  # Made path optional
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            response = input("Server reply > ")
            await websocket.send(response)
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain('cert.pem', 'key.pem')
    
    async with websockets.serve(
        handle_connection,
        "0.0.0.0", 
        8765,
        ssl=ssl_context
    ):
        print("Server running at wss://0.0.0.0:8765")
        await asyncio.Future()  # Run forever

asyncio.run(main())
