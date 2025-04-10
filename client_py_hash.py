import asyncio
import websockets
import ssl
import hmac
import hashlib

SECRET_KEY = b'my_private_key_123'  # Must match server's key

async def client():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        async with websockets.connect("wss://localhost:8765", ssl=ssl_context) as websocket:
            print("Connected to server! Type 'exit' to quit.")
            while True:
                message = input("Client message > ")
                if message.lower() == 'exit':
                    break
                
                # Create HMAC
                digest = hmac.new(SECRET_KEY, message.encode(), hashlib.sha256).hexdigest()
                print(f"Message HMAC: {digest}")
                
                await websocket.send(f"{message}|{digest}")
                response = await websocket.recv()
                
                if '|' in response:
                    resp_msg, resp_digest = response.split('|')
                    if hmac.compare_digest(resp_digest, hmac.new(SECRET_KEY, resp_msg.encode(), hashlib.sha256).hexdigest()):
                        print(f"Verified reply: {resp_msg}")
                    else:
                        print("Invalid server HMAC!")
                else:
                    print(f"Server response: {response}")
                    
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(client())
