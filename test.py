import database
import os.path


database.reset_db()
database.init_db()
assert os.path.exists("database.json")

print(database.get_db())

database.insert_task("Go to the grocery store")

print(database.get_db())

database.update_task(1, description="Go to the awesome store.")

print(database.get_db())

database.delete_task(1)

print(database.get_db())
