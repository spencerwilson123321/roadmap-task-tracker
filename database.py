import os.path
import json
import datetime

from enum import Enum


class TaskStatus(str, Enum):
    TODO = "to-do"
    IN_PROGRESS = "in-progress"
    DONE = "done"


def _get_db_filepath():
    root_path = os.path.dirname(os.path.abspath(__file__))
    database_filename = "database.json"
    db_filepath = os.path.join(database_filename)
    return db_filepath


def init_db():
    """
        Creates a json database if it doesn't already exist.
    """
    # Get the root of the project directory
    db_filepath = _get_db_filepath()
    # If it doesn't exist, we create an empty file.
    if not os.path.exists(db_filepath):
        with open(db_filepath, "w") as db:
            json.dump([], db)


def reset_db():
    db_filepath = _get_db_filepath()
    with open(db_filepath, "w") as db:
        json.dump([], db)




def _load_json():
    db_filepath = _get_db_filepath()
    db = []
    with open(db_filepath, "r") as f:
        db = json.load(f)
    assert isinstance(db, list)
    return db


def _save_db(db):
    db_filepath = _get_db_filepath()
    with open(db_filepath, "w") as f:
        json.dump(db, f)


def insert_task(description: str):
    if description is None:
        raise ValueError("description is missing")
    db = _load_json()
    db_filepath = _get_db_filepath()
    last_record = None
    if db:
        last_record = db[-1]
    next_task_id = 1
    if last_record:
        next_task_id = last_record["task_id"] + 1
    new_record = {
        "task_id": next_task_id,
        "description": description,
        "status": "to-do",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    db.append(new_record)
    _save_db(db)
    

def get_tasks():
    return _load_json()


def update_task(task_id: int, description=None, status=None):
    db = _load_json()
    for record in db:
        if record["task_id"] == task_id:
            if description is not None:
                record["description"] = description
            if status is not None:
                record["status"] = status
            record["updatedAt"] = datetime.datetime.now().isoformat()
    _save_db(db)


def delete_task(task_id: int):
    db = _load_json()
    for i, record in enumerate(db):
        if record["task_id"] == task_id:
            db.pop(i)
            break
    _save_db(db)


