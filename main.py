from fastapi import FastAPI
from utils import get_schedules, get_list_of_use, next_taking

app = FastAPI()



@app.get("/schedules")
async def schedules(user_id: int):
    result = get_schedules(user_id)
    return result


@app.get("/schedule")
async def schedules(user_id: int, schedule_id: int):
    result = get_list_of_use(user_id, schedule_id)
    return result


@app.get("/next_takings")
async def next_schedule(user_id: int):
    result = next_taking(user_id)
    return result


@app.post("/schedule")
async def create_schedule():
    return [{}]