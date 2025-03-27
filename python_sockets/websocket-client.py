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
        ) as ws:
            print("Connected to server!")
            while True:
                msg = input("Client message > ")
                if msg.lower() == 'exit':
                    break
                await ws.send(msg)
                response = await ws.recv()
                print(f"Server replied: {response}")
    except Exception as e:
        print(f"Connection failed: {e}")

asyncio.run(client())
