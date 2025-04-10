import asyncio
import websockets
import ssl
import hashlib
import hmac

PRIVATE_KEY = b"my_shared_secret_key"  # Must be same on client and server

def encrypt_message(message: str) -> str:
    # Create HMAC-SHA256 hash of the message
    hmac_digest = hmac.new(PRIVATE_KEY, message.encode(), hashlib.sha256).hexdigest()
    # Return original message + HMAC hash
    return f"{message}|{hmac_digest}"

async def client():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect('wss://localhost:8765', ssl=ssl_context) as ws:
        print("Connected! Type messages (or 'exit'):")
        while True:
            msg = input("> ")
            if msg.lower() == 'exit':
                break
            
            # Encrypt before sending
            encrypted_msg = encrypt_message(msg)
            print(f"Sending raw: {msg}")
            print(f"Sending encrypted: {encrypted_msg}")
            
            await ws.send(encrypted_msg)
            response = await ws.recv()
            print(f"Server response: {response}")

asyncio.get_event_loop().run_until_complete(client())
