import json
import os

# Filename where student data will be saved
DATA_FILE = "study_data.json"

def load_data():
    """Loads study tasks from a JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []  # Return empty list if no saved data exists

def save_data(tasks_list):
    """Saves the current study tasks to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks_list, f, indent=4)

# Initialize tasks list by loading saved data
# Each task is stored as a dictionary: {"title": "Math Review", "status": "Incomplete"}
tasks = load_data()

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
            for i, task in enumerate(tasks):
                print(f"{i + 1}. [{task['status']}] {task['title']}")
                
    elif choice == "2":
        new_title = input("\nEnter the subject or task to study: ")
        # Create a dictionary for the new task
        new_task = {"title": new_title, "status": "Incomplete"}
        tasks.append(new_task)
        save_data(tasks)  # Save changes instantly
        print(f"Saved: '{new_title}'")
        
    elif choice == "3":
        if not tasks:
            print("\nNo tasks available to complete.")
        else:
            print("\n--- SELECT TASK TO COMPLETE ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task['title']} ({task['status']})")
            
            try:
                task_num = int(input("\nEnter the number of the completed task: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["status"] = "COMPLETE"
                    save_data(tasks)  # Save changes instantly
                    print(f"Great job! '{tasks[task_num]['title']}' is marked complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        print("\nAll data safely saved. Good luck with your studies! Goodbye.")
        break
        
    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
