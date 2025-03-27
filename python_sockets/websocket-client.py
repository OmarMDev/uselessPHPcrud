import asyncio
import websockets
import ssl

async def client():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        async with websockets.connect(
            "wss://localhost:8765",
            ssl=ssl_context
        ) as websocket:
            print("Connected to server! Type 'exit' to quit.")
            while True:
                message = input("Client message > ")
                if message.lower() == 'exit':
                    await websocket.close()
                    break
                await websocket.send(message)
                response = await websocket.recv()
                print(f"Server replied: {response}")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(client())
