import asyncio
import websockets
import ssl

async def client():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    uri = "wss://localhost:8765"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        print("Connected to server")
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(client())
