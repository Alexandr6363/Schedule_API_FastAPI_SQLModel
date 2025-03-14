from sqlmodel import SQLModel, Field, Column, TIMESTAMP
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)


class Farma(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)


class Schedule(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    farma_id: int | None = Field(default=None, foreign_key="farma.id")    
    user_id: int | None = Field(default=None, foreign_key="user.id") 

    interval_in_min: int 
    is_constantly: bool 
    duration_in_days: int | None
    start_use: datetime = Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False
        ))