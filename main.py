from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/schedules")
async def schedules(user_id: int):
    return [{"user_id": user_id}]


@app.get("/schedule")
async def schedules(user_id: int, schedule_id: int):
    return [{"user_id": user_id, "schedule": schedule_id}]


@app.get("/next_takings")
async def next_taking(user_id: int):
    return [{"user_id": user_id}]