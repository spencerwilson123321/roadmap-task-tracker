import database
import cli
import os.path
import pytest
from argparse import Namespace


@pytest.fixture
def db():
    database.reset_db()
    database.init_db()
    yield None
    database.reset_db()
    

def test_db_exists(db):
    assert os.path.exists("database.json")


def test_insert_task(db):
    insert_args = Namespace(description="This is a test task")
    cli.insert_task(insert_args)
    tasks = database.get_tasks()
    assert len(tasks) >= 1


def test_update_task(db):
    insert_args = Namespace(description="This is a test task")
    cli.insert_task(insert_args)
    new_description = "This is a new description"
    update_args = Namespace(task_id=1, description=new_description)
    cli.update_task(update_args)
    tasks = database.get_tasks()
    assert tasks[0]["description"] == new_description

