#!/usr/bin/python3
import argparse
import database


def insert_task(args):
    database.init_db()
    database.insert_task(args.description)
    print("Created task")


def delete_task(args):
    database.init_db()
    database.delete_task(args.task_id)
    print("Deleted task")


def list_tasks(args):
    database.init_db()
    db = database.get_db()
    for record in db:
        if args.filter:
            if record["status"] == args.filter:
                print(f"Task ID: {record['task_id']} | Status: {record['status']} | Description: {record['description']} | createdAt: {record['createdAt']} | updatedAt: {record['updatedAt']}")
        else:
            print(f"Task ID: {record['task_id']} | Status: {record['status']} | Description: {record['description']} | createdAt: {record['createdAt']} | updatedAt: {record['updatedAt']}")


def mark_in_progress(args):
    database.init_db()
    database.update_task(args.task_id, status=database.TaskStatus.IN_PROGRESS)
    print("Marked task in progress")


def mark_done(args):
    database.init_db()
    database.update_task(args.task_id, status=database.TaskStatus.DONE)
    print("Marked task done")
    

def update_task(args):
    database.init_db()
    database.update_task(args.task_id, description=args.description)
    print("Updated task description")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Add command
    parser_insert = subparsers.add_parser("add")
    parser_insert.add_argument("description")
    parser_insert.set_defaults(func=insert_task)

    # Delete command
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("task_id", type=int)
    parser_delete.set_defaults(func=delete_task)

    # List command
    parser_list = subparsers.add_parser("list")
    valid_choices = [x.value for x in database.TaskStatus]
    parser_list.add_argument("filter", choices=valid_choices, nargs='?')
    parser_list.set_defaults(func=list_tasks)

    # Mark in progress command
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress")
    parser_mark_in_progress.add_argument("task_id", type=int)
    parser_mark_in_progress.set_defaults(func=mark_in_progress)

    # Mark as done command
    parser_mark_done = subparsers.add_parser("mark-done")
    parser_mark_done.add_argument("task_id", type=int)
    parser_mark_done.set_defaults(func=mark_done)

    # Update command
    parser_update = subparsers.add_parser("update")
    parser_update.add_argument("task_id", type=int)
    parser_update.add_argument("description")
    parser_update.set_defaults(func=update_task)

    args = parser.parse_args()
    
    func = getattr(args, "func", None)
    if func:
        func(args)
    else:
        parser.print_usage()

