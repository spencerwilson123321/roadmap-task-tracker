# roadmap-task-tracker
https://roadmap.sh/projects/task-tracker

# How to use:
Add a task
```
./cli.py add "Go to the grocery store"
```

List all tasks
```
./cli.py list
```

Delete a task
```
./cli.py delete 1
```

Update a task
```
./cli.py update 1 "Go to the video game store"
```

Mark tasks as in-progress or done
```
./cli.py mark-in-progress 1
./cli.py mark-done 1
```

List tasks, filter by status
```
./cli.py list done
./cli.py list to-do
./cli.py list in-progress
```

