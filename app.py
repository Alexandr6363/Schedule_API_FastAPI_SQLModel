from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, TIMESTAMP, Column, text


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
    
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()



if __name__ == "__main__":
    main()