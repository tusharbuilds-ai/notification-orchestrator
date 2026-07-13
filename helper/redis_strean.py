from typing import Dict
from core.redis import redis_client
from schemas.job_schema import JobSchema

STREAM_NAME = "notification_stream"


def publish_notification(payload:Dict)-> str:
    
    message_id = redis_client.xadd(
        STREAM_NAME,
        payload
    )

    return message_id