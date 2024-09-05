from fastapi import APIRouter

router = APIRouter()

@router.post("/backup")
def create_backup():
    return {"message": "Backup created successfully!"}
