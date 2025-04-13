# pydantic models

from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Optional", default=None)
    title: str = Field(min_length=3)
    category: str = Field(min_length=4)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "category": "Category name"
            }
        }
    }