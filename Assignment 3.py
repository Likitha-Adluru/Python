# List to store task details as dictionaries
tasks = [
    {'task_id': 1, 'description': 'Design project layout', 'status': 'pending', 'due_date': '2024-12-01'},
    {'task_id': 2, 'description': 'Develop login feature', 'status': 'in progress', 'due_date': '2024-11-20'},
    {'task_id': 3, 'description': 'Write user documentation', 'status': 'pending', 'due_date': '2024-11-25'},
    {'task_id': 4, 'description': 'Test payment system', 'status': 'completed', 'due_date': '2024-11-15'},
]

# Function to update task status
def update_task_status(task_id, new_status):
    for task in tasks:
        if task['task_id'] == task_id:
            task['status'] = new_status
            print(f"Task ID {task_id} status updated to {new_status}.")
            return
    print(f"Task ID {task_id} not found.")

# Function to update task due date
def update_task_due_date(task_id, new_due_date):
    for task in tasks:
        if task['task_id'] == task_id:
            task['due_date'] = new_due_date
            print(f"Task ID {task_id} due date updated to {new_due_date}.")
            return
    print(f"Task ID {task_id} not found.")

# Function to generate report grouped by task status
def generate_report():
    # Creating dictionaries to hold tasks by status
    report = {'pending': [], 'in progress': [], 'completed': []}
    
    for task in tasks:
        if task['status'] == 'pending':
            report['pending'].append(task)
        elif task['status'] == 'in progress':
            report['in progress'].append(task)
        elif task['status'] == 'completed':
            report['completed'].append(task)
    
    # Display report
    print("\n--- Task Report Grouped by Status ---")
    for status, task_list in report.items():
        print(f"\nStatus: {status.capitalize()}")
        if task_list:
            for task in task_list:
                print(f"Task ID: {task['task_id']}, Description: {task['description']}, Due Date: {task['due_date']}")
        else:
            print("No tasks in this status.")
    
# Test: Update task statuses, due dates, and generate report
update_task_status(1, 'completed')  # Update task ID 1 status to 'completed'
update_task_due_date(2, '2024-12-05')  # Update task ID 2 due date

# Generate report of tasks grouped by their status
generate_report()

# Additional test: Assign a task based on due date
def assign_task_based_on_due_date(due_date):
    for task in tasks:
        if task['due_date'] == due_date:
            print(f"Task assigned: ID {task['task_id']}, Description: {task['description']}, Due Date: {task['due_date']}")
            return
    print(f"No task found with the due date {due_date}.")

# Example: Assign task with a specific due date
assign_task_based_on_due_date('2024-11-20')
