import asyncio
import websockets
import ssl

async def send_messages():
    ssl_context = ssl.SSLContext(ssl.PTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect('wss://localhost:8765', ssl=ssl_context) as ws:
        while True:
            message = input("Message to send: ")
            await ws.send(message)
            response = await ws.recv()
            print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(send_messages())
