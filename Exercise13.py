import os 

file_name = "tasks.txt"

def load_tasks():
    tacks = {}
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            for line in file:
                task_id,title,status = line.strip().strip("|")
                tacks[int(tack_id)] = {"title":title,"status": status}
    return tacks

#save tasks to file
def save_tasks(tacks):
    with open(file_name,"w") as file:
        for task_id,task in task.item():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
            

# add a new task
def add_task(tacks):
    title = input("Enter task title: ")
    task_id = max(tasks.key(),default = 0) + 1
    tacks[tack_id] = {"title":title,"status": "incomplete"}
    print(f"task '{title}' added.")
 
#view all tasks 
def view_tasks(tacks):
    if not tasks:
        print("No task available.")
    else:
        for task_id, task in task.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task Id to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task id not found.")
        
#delete a task 
def delete_task(tasks):
    task_id = int(input("Enter the task id to delete: "))
    if task_id in tasks:
        delete_task = task.pop(task_id)
        print(f"task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task id not found.")

#main menu
def main():
    task = load_tasks()
    while True:
        print("\n Task manager menu: ")
        print("1. Add task")
        print("2. View task")
        print("3. Mark Task to complete")
        print("4. Delete task")
        print("5. Exit")  
        choice = int(input("Enter the choice: "))

        if choice == '1':
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)        
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Good bye")
            break
        else:
            print("Invalide Choice. Please try again")
            
            
if __name__ == "__main__":
    main()
    