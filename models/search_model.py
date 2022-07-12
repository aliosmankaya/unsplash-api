from pydantic import BaseModel, Field
from typing import Optional


class Search(BaseModel):
    query: Optional[str] = Field(default="nature")
    page: Optional[int] = Field(default=1)
    per_page: Optional[int] = Field(default=10)
    order_by: Optional[str] = Field(default="relevant")
