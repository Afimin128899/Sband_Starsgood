import requests
from config import FLYER_API_KEY, FLYER_BASE_URL

HEADERS = {"X-API-Key": FLYER_API_KEY}

def get_task(user_id):
    r = requests.get(
        f"{FLYER_BASE_URL}/tasks/get",
        headers=HEADERS,
        params={"user_id": user_id, "platform": "telegram"},
        timeout=10
    )
    return r.json()

def check_task(task_id, user_id):
    r = requests.get(
        f"{FLYER_BASE_URL}/tasks/check",
        headers=HEADERS,
        params={"task_id": task_id, "user_id": user_id},
        timeout=10
    )
    return r.json()
