from fastapi import (
    APIRouter, Depends,
)

from mainApi.app.auth.auth import get_current_user
from mainApi.app.cellpose.sub_routers.views.routers import router as view_router

router = APIRouter(
    prefix="/cellpose",
    tags=[],
    dependencies=[Depends(get_current_user)]
)

router.include_router(view_router)
