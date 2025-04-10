import asyncio
import websockets
import ssl
import hmac
import hashlib

SECRET_KEY = b'my_private_key_123'  # Must be the same on client and server

async def handler(websocket):
    print("Client connected!")
    try:
        while True:
            message = await websocket.recv()
            print(f"Raw message: {message}")
            
            # Verify HMAC
            received_msg, received_digest = message.split('|')
            computed_digest = hmac.new(SECRET_KEY, received_msg.encode(), hashlib.sha256).hexdigest()
            
            if hmac.compare_digest(received_digest, computed_digest):
                print(f"Verified message: {received_msg}")
                response = input("Server response > ")
                
                # Create HMAC for response
                response_digest = hmac.new(SECRET_KEY, response.encode(), hashlib.sha256).hexdigest()
                await websocket.send(f"{response}|{response_digest}")
            else:
                await websocket.send("INVALID HMAC")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain('cert.pem', 'key.pem')

    async with websockets.serve(handler, "0.0.0.0", 8765, ssl=ssl_context):
        print("Server running at wss://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
