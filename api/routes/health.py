from fastapi import APIRouter
from schemas.return_schema import ApiResponse
router = APIRouter()


@router.get("")
def health():
    return ApiResponse(
        success=True,
        message="Sever is healthy"
    )