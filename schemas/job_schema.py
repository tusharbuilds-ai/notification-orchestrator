from pydantic import BaseModel
from typing import Optional
import uuid


class JobSchema(BaseModel):
    job_id:str
    message:str
    channels:list
