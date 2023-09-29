import datetime as dt

import pydantic as pydantic
from pydantic import BaseModel, HttpUrl


class UserBase(pydantic.BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True


class LeadBase(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    note: str


class LeadCreate(LeadBase):
    pass


class Lead(LeadBase):
    id: int
    owner_id: int
    date_created: dt.datetime
    date_last_updated: dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True

class GetInfoAboutLinkResponse(BaseModel):
    long_url: HttpUrl
    number_of_clicks: int
    dt_created: dt

    class Config:
        orm_mode = True