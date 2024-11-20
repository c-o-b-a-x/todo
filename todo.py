import json

def get_data():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("Invalid JSON")

def save_tasks(data):
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

def add_task(data, number, task):
    data.append({"task": task, "number": number, "status": "incomplete"})
    data.sort(key=lambda x: x['number'])
    save_tasks(data)
    return data

def view_tasks(data):
    for task in data:
        print(f"Number: {task['number']} , task: {task['task']}")

def status_tasks(data, status):
    for task in data:
        if task['status'] == status:
            print(f'{status}:{task["task"]} number: {task["number"]}')

def change_status(data):
    number = input("What number task would you like to change: ")
    for task in data:
        if str(task['number']) == number:
            task['status'] = 'complete'
            save_tasks(data)
            break

def action1(data):
    status = "complete"
    status_tasks(data, status)
def action2(data):
    status = "incomplete"
    status_tasks(data, status)

def action5(data):
    number = len(data) + 1
    task = input("What task would you like to add: ")
    add_task(data, number, task)
    view_tasks(data)
def get_input(data):
    while True:
        action = input("""Please choose an option:\n1. View completed tasks\n2. View incomplete tasks \n 3. View all tasks \n 4. Mark a task as complete\n5. Add a new task\n6. Quit\n choice: """)
        try:
            action = int(action)
            if action == 1:
                action1(data)
            elif action == 2:
                action2(data)
            elif action == 3:
                view_tasks(data)
            elif action == 4:
                change_status(data)
            elif action == 5:
                action5(data)
            elif action == 6:
                quit()
            else:
                print("invalid choice")
        except ValueError:
            print("invalid choice")

def main():
    data = get_data() or []
    get_input(data)

if __name__ == '__main__':
    main()
