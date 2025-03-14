from datetime import datetime
from sqlmodel import Session, SQLModel, create_engine, Field, Column, TIMESTAMP
from models import *
from data import *


    
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



def fill_db(list_of_data):
    for item in list_of_data:
        with Session(engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            print(item)


def create_some_schedules():
    pass

def main():
    create_db_and_tables()
    fill_db(user_list)
    fill_db(farm_list)
    fill_db(schedule_list)


if __name__ == "__main__":
    main()