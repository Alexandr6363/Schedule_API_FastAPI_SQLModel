from sqlmodel import SQLModel, create_engine
from .utils import fill_db 
from .config import DATABASE_NAME


    
sqlite_file_name = DATABASE_NAME
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_and_fill_db():
    create_db_and_tables()
    fill_db()
    
