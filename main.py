import json

tasks=[]
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
        inpt0=int(input('Enter The Number: '))

        if inpt0 == 1:
            task_name=input("Enter The Task: ").strip()
            if task_name=="":
                print("-Task can't be empty!-")
            else:
                tasks.append({'name':task_name,'mark':False})
                print("-Task Added-")

        elif inpt0 == 2:
            if not tasks:
                print("-No Task-")
            else:
                task_number=int(input('Enter The Number Task: '))
                tasks.pop(task_number -1)
                print("-Task Removed-")

        elif inpt0 == 3:
            for number, task in enumerate(tasks, start=1):
                if task['mark']:
                    mark="*"
                else:
                    mark=" "
                print(f"{number}.{task['name']} [{mark}]")
            if tasks == []:
                print("-No Task-")

        elif inpt0 == 4:
            task_number=int(input('Enter The Number Task: '))
            tasks[task_number -1]['mark'] = not tasks[task_number -1]['mark']
            print('-Task Marked-')

        elif inpt0 == 5:
            tasks.clear()
            print("-Removed All Task-")

        elif inpt0 == 6:
            print("-Exited-")
            break
        
        else:
            print("Invalid option-")

    except ValueError:
        print("-Please enter a number!-")
    except IndexError:
        print("-Task not found!-")