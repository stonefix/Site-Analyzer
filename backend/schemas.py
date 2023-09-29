import datetime as _dt

import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True


class _LeadBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    note: str


class LeadCreate(_LeadBase):
    pass


class Lead(_LeadBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True
        allow_population_by_field_name = True
