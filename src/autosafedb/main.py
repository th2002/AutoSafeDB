from fastapi import FastAPI
from src.autosafedb.api.v1.backup import router as backup_router

app = FastAPI()

# Register API routes
app.include_router(backup_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoSafeDB!"}

