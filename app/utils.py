from .data import user_list, farm_list, schedule_list
from sqlmodel import Session, create_engine, SQLModel, select
from .models import User, Farma, Schedule
from .config import DATABASE_NAME


sqlite_file_name = DATABASE_NAME
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def fill_table(list_of_data):
    for item in list_of_data:
        with Session(engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            print(item)

def fill_db():
    fill_table(user_list)
    fill_table(farm_list)
    fill_table(schedule_list)


def get_schedules(user_id):
    with Session(engine) as session:
        statement = select(Schedule).where(Schedule.user_id == int(user_id))
        result = session.exec(statement)
        response = []
        for schedule in result:
            response.append(
                schedule.id
            )
        return response

def get_list_of_use(user_id, schedule_id):
    with Session(engine) as session:
        statement = select(Schedule).where(Schedule.user_id == int(user_id)).where(Schedule.id == schedule_id)
        result = session.exec(statement)
        response = result.one_or_none()
        if response:
            response = response.list_of_use()
        else:
            response = []
        return response
    
def next_taking(user_id):
    with Session(engine) as session:
        statement = select(Schedule).where(Schedule.user_id == int(user_id))
        result = session.exec(statement)
        response = []
        for schedule in result:
            if schedule.next_time_schedule():
                response.append({
                    "farma": schedule.farma.name,
                    "schedule": schedule.next_time_schedule(),
                })
                            
        return response
    

def find_or_create_farma(farma_name):
    with Session(engine) as session:
        statement = select(Farma).where(Farma.name == farma_name)
        result = session.exec(statement)
        farma = result.one_or_none()

        if farma:
            return farma.id
        else:
            farma = Farma(name=farma_name)
            session.add(farma)
            session.commit()
            return farma.id

def create_new_schedule(data):
    with Session(engine) as session:
        new_schedule = Schedule(**data)
        session.add(new_schedule)
        session.commit()
        session.refresh(new_schedule)
        return new_schedule
