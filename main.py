import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


print("---------------------------")
print("|    -=First Mark=-       |")
print("| 1.Add Task              |")
print("| 2.Remove Task           |")
print("| 3.Show Tasks            |")
print("| 4.Mark Task             |")
print("| 5.Remove All Task       |")
print("| 6.Exit                  |")
print("---------------------------")


while True:
    try:
        inpt0 = int(input("Enter The Number: "))

        if inpt0 == 1:
            task_name = input("Enter The Task: ").strip()

            if task_name == "":
                print("-Task can't be empty!-")
            else:
                tasks.append({
                    "name": task_name,
                    "mark": False
                })

                save_tasks()
                print("-Task Added-")

        elif inpt0 == 2:
            if not tasks:
                print("-No Task-")
            else:
                task_number = int(input("Enter The Number Task: "))

                if 1 <= task_number <= len(tasks):
                    tasks.pop(task_number - 1)
                    save_tasks()
                    print("-Task Removed-")
                else:
                    print("-Task not found!-")

        elif inpt0 == 3:
            if not tasks:
                print("-No Task-")
            else:
                for number, task in enumerate(tasks, start=1):
                    if task["mark"]:
                        mark = "*"
                    else:
                        mark = " "

                    print(f"{number}.{task['name']} [{mark}]")

        elif inpt0 == 4:
            if not tasks:
                print("-No Task-")
            else:
                task_number = int(input("Enter The Number Task: "))

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["mark"] = not tasks[task_number - 1]["mark"]
                    save_tasks()
                    print("-Task Marked-")
                else:
                    print("-Task not found!-")

        elif inpt0 == 5:
            tasks.clear()
            save_tasks()
            print("-Removed All Task-")

        elif inpt0 == 6:
            print("-Exited-")
            break

        else:
            print("-Invalid option-")

    except ValueError:
        print("-Please enter a number!-")