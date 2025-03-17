from sqlmodel import SQLModel, Field, Column, TIMESTAMP, Relationship
from datetime import datetime, timedelta
import math
from config import NEXT_TIME_HOURS


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    schedules: list["Schedule"] = Relationship(back_populates="user")


class Farma(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    schedules: list["Schedule"] = Relationship(back_populates="farma")    


class Schedule(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    farma_id: int | None = Field(default=None, foreign_key="farma.id")
    farma: Farma | None = Relationship(back_populates="schedules")

    user_id: int | None = Field(default=None, foreign_key="user.id") 
    user: User | None = Relationship(back_populates="schedules")

    interval_in_min: int 
    is_constantly: bool 
    duration_in_days: int | None
    start_use: datetime = Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False
        ))
    

    def finish_of_use(self):
        if self.is_constantly:
            return ""
        return self.start_use + timedelta(days=self.duration_in_days)

    def list_of_use(self):

        def round_time(time):
            hours, minutes = divmod(math.ceil(time.minute/15)*15, 60)
            rounded_time = (time + timedelta(hours=hours)).replace(minute=minutes)
            return rounded_time
            
        today = datetime.today()
        dayly_schedule = []

        if not self.is_constantly and self.finish_of_use() <= today:
            return dayly_schedule
        else:
            start_time = datetime(today.year, today.month, today.day, 8, 0)
            finish_time = datetime(today.year, today.month, today.day, 22, 0)
            current_time = start_time
            while current_time <= finish_time:                
                dayly_schedule.append(round_time(current_time))
                current_time += timedelta(minutes=self.interval_in_min)
        return dayly_schedule
    
    def next_time_schedule(self):
        start_time = datetime.today().now()
        finish_time = start_time + timedelta(hours=NEXT_TIME_HOURS)
        next_time_list = []
        for element in self.list_of_use():
            if element >= start_time and element <= finish_time:
                next_time_list.append(element)
        return  next_time_list