import argparse
import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), '..', 'tasks.json')


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def add_task(task_text):
    tasks = load_tasks()
    tasks.append({'task': task_text, 'done': False})
    save_tasks(tasks)
    print(f"✅ Added task: {task_text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "❌"
        print(f"{i}. {status} {t['task']}")


def mark_done(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]['done'] = True
    save_tasks(tasks)
    print(f"✅ Marked task {index} as done.")


def main():
    parser = argparse.ArgumentParser(description="Todo CLI App")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all tasks")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", help="The task description")

    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("index", type=int, help="Task number")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.text)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.index)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()