def add_task(tasks, title):
    """Append a new task to the list and return it."""
    tasks.append({"title": title, "done": False})
    return tasks

def complete_task(tasks, index):
    """Mark the task at the given position (1-based) as done."""
    tasks[index - 1]["done"] = True
    return tasks

 
def main():
    tasks = []
    add_task(tasks, "Set up repository")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']}")
 
if __name__ == "__main__":
    main()
