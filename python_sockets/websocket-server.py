import asyncio
import websockets
import ssl

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Server echoes: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

start_server = websockets.serve(echo, "0.0.0.0", 8765, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
