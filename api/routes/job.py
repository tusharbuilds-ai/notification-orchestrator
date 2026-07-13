from fastapi import APIRouter
from schemas.job_schema import JobSchema
from schemas.return_schema import ApiResponse
from helper.redis_strean import publish_notification

router = APIRouter()


@router.post("")
def create_job(payload:JobSchema):

    payload.channels = ",".join(payload.channels)

    message_id = publish_notification(
            payload.model_dump(mode="json")
        )

    return ApiResponse(
        success=True,
        message="Message added to the stream",
        data=message_id
    )