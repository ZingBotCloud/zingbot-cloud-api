from fastapi import APIRouter

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)


@router.get("/")
def list_workspaces():
    return {
        "workspaces": []
    }


@router.post("/create")
def create_workspace():
    return {
        "message": "Workspace created successfully"
    }
