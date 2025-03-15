from fastapi import FastAPI
from utils import get_schedules

app = FastAPI()



@app.get("/schedules")
async def schedules(user_id: int):
    result = get_schedules(user_id)
    return result


@app.get("/schedule")
async def schedules(user_id: int, schedule_id: int):
    return [{"user_id": user_id, "schedule": schedule_id}]


@app.get("/next_takings")
async def next_taking(user_id: int):
    return [{"user_id": user_id}]


@app.post("/schedule")
async def create_schedule():
    return [{}]