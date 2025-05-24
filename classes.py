from typing import Optional, Annotated

from pydantic import BaseModel, Field


class Pizza(BaseModel):
    name: str
    price: float = Field(gt=0)


class Location(BaseModel):
    city: str
    state: str
    country: Optional[str] = None


class User(BaseModel):
    name: str
    age: int
    location: Optional[Location] = None
    bike: str
    rides: list[Annotated[int, Field(gt=0)]] = Field(default_factory=list[Annotated[int, Field(gt=0)]])
