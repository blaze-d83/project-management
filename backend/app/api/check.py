from fastapi import APIRouter, status


health_check_router = APIRouter()


@health_check_router.get("/check", status_code=status.HTTP_200_OK)
def check_status():
    return {"Hello World"}
