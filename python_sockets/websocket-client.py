import asyncio
import websockets
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def client():
    async with websockets.connect('wss://localhost:8765', ssl=ssl_context) as ws:
        print("Connected! Type messages, or 'exit' to quit.")
        while True:
            msg = input("> ")
            if msg == 'exit':
                break
            await ws.send(msg)
            print(await ws.recv())

asyncio.get_event_loop().run_until_complete(client())
