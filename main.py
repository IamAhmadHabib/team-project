def add_task(tasks, title):
    """Append a new task to the list and return it."""
    tasks.append({"title": title, "done": False})
    return tasks
 
def main():
    tasks = []
    add_task(tasks, "Set up repository")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']}")
 
if __name__ == "__main__":
    main()
