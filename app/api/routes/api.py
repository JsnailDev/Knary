from fastapi import APIRouter

from app.api.routes import auth_route, user_route


router = APIRouter()
router.include_router(auth_route.router, tags=["authentication"], prefix="/users")
router.include_router(user_route.router, tags=["users"], prefix="/user")
