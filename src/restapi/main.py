from pathlib import Path
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Define the paths to your certificate and key
path_cert = Path(__file__).parent.parent.parent
certfile = f'{path_cert}/certs/cert.pem'
keyfile = f'{path_cert}/certs/key.pem'

@app.get("/")
async def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        ssl_certfile=certfile,
        ssl_keyfile=keyfile
    )
