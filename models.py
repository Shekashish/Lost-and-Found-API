from typing import Literal

from pydantic import field_validator
from sqlmodel import Field, SQLModel


# Request model: validates incoming data
class ItemCreate(SQLModel):
    title: str
    description: str
    category: str
    location: str
    reported_by: str
    status: Literal["Lost", "Found", "Returned"] = "Lost"

    @field_validator("title", "description", "category", "location", "reported_by")
    @classmethod
    def validate_text(cls, value: str):
        if not value or not value.strip():
            raise ValueError("This field cannot be empty")
        return value.strip()


# Database model
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    location: str
    reported_by: str
    status: str = "Lost"
