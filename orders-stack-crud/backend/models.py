#Este archivo define la estructura de los datos usando Pydantic.
#Pydantic valida automáticamente los datos que llegan a la API

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any
from bson import ObjectId


class Task(BaseModel):
    id: Optional[str] = Field(default=None, alias='_id')
    title: str
    description: Optional[str] = None
    completed: bool = False

    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid_to_str(cls, v: Any):
        if v is None:
            return None
        # si viene de Mongo como ObjectId -> str
        if isinstance(v, ObjectId):
            return str(v)
        # si viene como string ya, lo dejamos
        return str(v)

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
