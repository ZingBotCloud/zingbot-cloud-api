from fastapi import FastAPI
import auth

app = FastAPI(
    title="ZingBot Cloud API",
    version="1.0.0",
    description="Official Backend API for ZingBot Cloud"
)

app.include_router(auth.router)


@app.get("/")
def home():
    return {
        "name": "ZingBot Cloud API",
        "version": "1.0.0",
        "status": "online",
        "message": "Welcome to ZingBot Cloud 🚀"
    }
