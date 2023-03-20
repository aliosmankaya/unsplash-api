from pydantic import BaseModel, Field
from typing import Optional


class Random(BaseModel):
    query: Optional[str] = Field(default="nature")
    count: Optional[int] = Field(default=1)
