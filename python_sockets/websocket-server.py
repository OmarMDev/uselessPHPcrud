import asyncio
import websockets
import ssl

async def handler(websocket, path):
    print("Client connected!")
    try:
        while True:
            message = await websocket.recv()
            print(f"Got: {message}")
            await websocket.send("Server received: " + message)
    except:
        print("Client disconnected")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

start_server = websockets.serve(handler, "0.0.0.0", 8765, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
