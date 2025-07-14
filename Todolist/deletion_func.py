def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            del tasks["tasks"][task_number - 1]
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")
