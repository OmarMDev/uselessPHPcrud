import asyncio
import websockets
import ssl
import hashlib
import hmac

PRIVATE_KEY = b"my_shared_secret_key"  # Must match client key

def verify_message(encrypted_msg: str) -> tuple:
    try:
        message, received_hmac = encrypted_msg.split("|")
        # Recompute HMAC
        expected_hmac = hmac.new(PRIVATE_KEY, message.encode(), hashlib.sha256).hexdigest()
        
        if hmac.compare_digest(received_hmac, expected_hmac):
            return True, message
        return False, "HMAC verification failed"
    except:
        return False, "Invalid message format"

async def handler(websocket):
    print("Client connected!")
    try:
        async for encrypted_msg in websocket:
            print(f"Received encrypted: {encrypted_msg}")
            
            # Verify and decrypt
            is_valid, message = verify_message(encrypted_msg)
            
            if is_valid:
                print(f"Decrypted message: {message}")
                await websocket.send(f"ACK: {message}")
            else:
                print(f"Invalid message: {message}")
                await websocket.send("ERROR: Invalid message")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

start_server = websockets.serve(handler, "0.0.0.0", 8765, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
