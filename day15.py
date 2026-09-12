#creating a small project
starting = input("Do you want to start the project? (yes/no): ")
if starting == "yes":
    print("Project started!")
else:
    print("Project not started.")


while True:
    task = input("Enter a task to add to the project (or type 'exit' to finish): ")
    if task.lower() == "exit":
        break
    else:
        print(f"Task '{task}' added to the project.")
#now listing the tasks
tasks = ["Task 1: Set up the environment", "Task 2: Create the main module", "Task 3: Implement the features", "Task 4: Test the application", "Task 5: Deploy the project"]
print("\nHere are the tasks for the project:")
for task in tasks:
    print(task)