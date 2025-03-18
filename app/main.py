from fastapi import FastAPI
from .utils import get_schedules, get_list_of_use, next_taking, find_or_create_farma, create_new_schedule
from datetime import datetime
from .create_and_fill_db import create_and_fill_db



create_and_fill_db()

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
async def create_schedule(
    farma_name: str,
    user_id: int,
    is_constantly: bool,
    interval_in_min: int,
    duration_in_days: int | None = None

):
    farma_id = find_or_create_farma(farma_name)

    data = {
        "farma_id": farma_id,
        "user_id": user_id,
        "is_constantly": is_constantly,
        "interval_in_min": interval_in_min,
        "start_use": datetime.now(),
    }

    if duration_in_days:
        data["duration_in_days"] = duration_in_days

    create_new_schedule(data)
    return data