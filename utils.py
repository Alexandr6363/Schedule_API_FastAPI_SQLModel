from data import user_list, farm_list, schedule_list
from sqlmodel import Session, create_engine, SQLModel, select
from models import User, Farma, Schedule


sqlite_file_name = "database.db"
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
            #     {
            #     "user": schedule.user,
            #     "farma": schedule.farma,
            #     "schedule_id": schedule.id,
            #     "schedule_finish_date": schedule.finish_of_use(),
            #     "schedule_list_of_use": schedule.list_of_use(),
            #     "schedule_next_time_schdule": schedule.next_time_schedule(),
            # }
            )
        return response
