from fastapi import FastAPI, Response
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse
import hashlib

app = FastAPI()


@app.post("/encode")
async def encode(url: str):
    if not url:
        raise HTTPException(detail="URL is required", status_code=400)
    parsed_url = urlparse(url)

    if not(parsed_url.scheme and parsed_url.netloc):
        raise HTTPException(detail="URL is invalid", status_code=400)

    hasher = hashlib.sha256()
    hasher.update(url.encode())
    return Response(content=hasher.hexdigest(), status_code=200)
