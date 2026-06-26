FILE_NAME = "tasks.txt"

print("----- TO DO LIST -----")

while True:

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Choice : ")

    match(choice):

        # ADD TASK
        case "1":

            task = input("Enter Task : ")

            with open(FILE_NAME, "a") as file:
                file.write(task + "\n")

            print("Task Added Successfully")

        # VIEW TASKS
        case "2":

            try:
                with open(FILE_NAME, "r") as file:

                    tasks = file.readlines()

                    if len(tasks) == 0:
                        print("No Tasks Available")

                    else:
                        print("\nYour Tasks :")

                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task.strip()}")

            except FileNotFoundError:
                print("No Tasks Available")

        # DELETE TASK
        case "3":

            try:
                with open(FILE_NAME, "r") as file:
                    tasks = file.readlines()

                if len(tasks) == 0:
                    print("No Tasks To Delete")

                else:

                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")

                    delete = int(input("Enter Task Number : "))

                    if 1 <= delete <= len(tasks):

                        removed = tasks.pop(delete - 1)

                        with open(FILE_NAME, "w") as file:
                            file.writelines(tasks)

                        print(f"{removed.strip()} Deleted Successfully")

                    else:
                        print("Invalid Task Number")

            except FileNotFoundError:
                print("No Tasks Available")

        # EXIT
        case "4":
            print("Thanks For Using To Do List")
            break

        # INVALID CHOICE
        case _:
            print("Invalid Choice")