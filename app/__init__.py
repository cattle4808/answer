from fastapi import APIRouter

from . import answer, script

router = APIRouter()
router.include_router(answer.router, prefix="/answer", tags=["answer"])
router.include_router(script.router, prefix="/script", tags=["script"])

__all__ = ["router"]