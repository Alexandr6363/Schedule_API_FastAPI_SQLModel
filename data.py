from models import *
from datetime import datetime

farm_list = [
    Farma(name="Vitamin A"),
    Farma(name="Vitamin B"),
    Farma(name="Vitamin C"),
    Farma(name="Protein"),
    Farma(name="BCAA")
]  

user_list = [
    User(name="Anna"),
    User(name="Kate"),
    User(name="Alex"),
]


schedule_list = [
    Schedule(
        farma_id=1,
        user_id=1,
        interval_in_min=600,
        is_constantly=True,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=1,
        farma_id=2,
        interval_in_min=500,
        is_constantly=False,
        duration_in_days=3,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=1,
        farma_id=3,
        interval_in_min=1250,
        is_constantly=True,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=2,
        farma_id=4,
        interval_in_min=65,
        is_constantly=False,
        duration_in_days=7,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=2,
        farma_id=2,
        interval_in_min=300,
        is_constantly=False,
        duration_in_days=4,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=2,
        farma_id=5,
        interval_in_min=1500,
        is_constantly=False,
        duration_in_days=15,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=2,
        farma_id=2,
        interval_in_min=500,
        is_constantly=False,
        duration_in_days=10,
        start_use=datetime.now(),
     ),    
    Schedule(
        user_id=3,
        farma_id=3,
        interval_in_min=50,
        is_constantly=False,
        duration_in_days=4,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=3,
        farma_id=5,
        interval_in_min=670,
        is_constantly=False,
        duration_in_days=15,
        start_use=datetime.now(),
     ),
    Schedule(
        user_id=3,
        farma_id=1,
        interval_in_min=100,
        is_constantly=True,
        start_use=datetime.now(),
     ),    
]
