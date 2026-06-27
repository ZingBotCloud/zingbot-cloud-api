from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
def auth_home():
    return {
        "message": "Authentication service is running"
    }


@router.get("/login")
def login():
    return {
        "status": "Coming soon"
    }


@router.get("/register")
def register():
    return {
        "status": "Coming soon"
    }
