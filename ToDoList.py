def display_options():
    print("""
    Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

#functions to handle input of integers and text

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Did not enter a number. Try again...")

def get_text(prompt):
    while True:
        try:
            text=input(prompt)
            if len(text)<1:
                raise ValueError("Task must not be empty string. Try again: ")
            else:
                return text
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print("Unexpected error occurred.", e)

#functions to manipulate and view to-do list
#appends tuple ("Task", "Incomplete")

def task_add(list):
    list.append((get_text("Please Enter your task"), "Incomplete"))

def view_tasks(list):
    if not len(list):
        print("To-Do List is empty")
    for index, (task, status) in enumerate(list):
        print(f"#{index} | Task: {task} | Status: {status}")

def task_complete(list):
    if len(list):
        while True:
            try:
                view_tasks(list)
                index=get_number("Please enter the number of the task you wish to mark complete")
                if index<0 or index > len(list):
                    raise ValueError("Invalid Index. Please try again")
            except ValueError as e:
                print(e)
            else:
                list[index]= (list[index][0], "Complete")
                print(f"Task #{index} has been marked complete.")
                break
    else:
        print("To-Do List is empty")

def task_delete(list):
    if len(list):
        while True:
            try:
                index=get_number("Please enter the number of the task you wish to delete")
                if index<0 or index > len(list):
                    raise ValueError("Invalid Index. Please try again")
            except ValueError as e:
                print(e)
            else:
                del list[index]
                print(f"Task #{index} has been deleted")
                break
    else:
        print("To-Do List is already empty")


def main():
    to_do_list=[]
    while True:
        display_options()
        choice = get_number("Please enter your choice: ")
        if choice == 1:
            task_add(to_do_list)
        elif choice == 2:
            view_tasks(to_do_list)
        elif choice == 3:
            task_complete(to_do_list)
        elif choice == 4:
            task_delete(to_do_list)
        elif choice == 5:
            print("Exiting To-Do List App. Thanks for using it")
            break
        else:
            print("Invalid choice. Please try again.")

main()