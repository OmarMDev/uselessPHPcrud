import asyncio
import websockets
import ssl

# The handler now properly accepts both websocket and path
async def handler(websocket, path):
    print("Client connected!")
    try:
        while True:
            message = await websocket.recv()
            print(f"Received from client: {message}")
            response = input("Server response > ")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    # SSL setup
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain('cert.pem', 'key.pem')

    # Start server
    async with websockets.serve(
        handler,
        "0.0.0.0",
        8765,
        ssl=ssl_context
    ):
        print("Server running at wss://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
