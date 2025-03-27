import asyncio
import websockets
import ssl

async def handle_connection(websocket):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            response = input("Server response > ")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    server = await websockets.serve(
        handle_connection,
        "0.0.0.0",
        8765,
        ssl=ssl_context
    )
    print(f"WebSocket SSL server running on wss://0.0.0.0:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
