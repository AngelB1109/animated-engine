# Student Study Planner & To-Do List

# Lists to store our study tasks and status
tasks = []
status = []

print("=== WELCOME TO THE STUDENT STUDY PLANNER ===")

while True:
    print("\nOptions:")
    print("1. View Study Tasks")
    print("2. Add a Study Task")
    print("3. Mark Task as Complete")
    print("4. Exit")
    
    choice = input("\nChoose an option (1-4): ")
    
    if choice == "1":
        if not tasks:
            print("\nYour study list is empty!")
        else:
            print("\n--- YOUR STUDY LIST ---")
            for i in range(len(tasks)):
                print(f"{i + 1}. [{status[i]}] {tasks[i]}")
                
    elif choice == "2":
        new_task = input("\nEnter the subject or task to study: ")
        tasks.append(new_task)
        status.append("Incomplete")
        print(f"Added: '{new_task}'")
        
    elif choice == "3":
        if not tasks:
            print("\nNo tasks available to complete.")
        else:
            print("\n--- SELECT TASK TO COMPLETE ---")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            
            try:
                task_num = int(input("\nEnter the number of the completed task: ")) - 1
                if 0 <= task_num < len(tasks):
                    status[task_num] = "COMPLETE"
                    print(f"Great job! '{tasks[task_num]}' is marked complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        print("\nGood luck with your studies! Goodbye.")
        break
        
    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
