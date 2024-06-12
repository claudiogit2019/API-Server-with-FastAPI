from fastapi import FastAPI, status
import uuid

from models import User

app = FastAPI()

users = {
    "1": {
        "name": "John",
        "age": 20
    },
    "2": {
        "name": "Jane",
        "age": 21
    }
}

@app.get("/users")
def users_list():
    return users

@app.get("/users/{user_id}")
def user_details(user_id: str):
    return users[user_id]

@app.post("/users", status_code=status.HTTP_201_CREATED)
def user_add(user: User):
    users[str(uuid.uuid4())] = user
    return "User added"

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_update(user_id: str, user: User):
    users[user_id] = user
    return "User updated"

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_delete(user_id: str):
    del users[user_id]
    return "User deleted"

