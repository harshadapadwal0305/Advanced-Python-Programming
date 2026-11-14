# ---------------- DECORATOR ----------------
def decorate(fun):
    def inner():
        print("Processing tasks...")
        fun()
        print("Done")
    return inner


# ---------------- EMPLOYEE ----------------
class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department
        self.tasks = []
    def get_role_details(self):
        return "Employee"
    def add_task(self, task):
        self.tasks.append(task)


# ---------------- DEVELOPER ----------------
class Developer(Employee):
    def __init__(self, id, name, department, language):
        super().__init__(id, name, department)
        self.language = language
    def get_role_details(self):
        return "Developer - " + self.language


# ---------------- DATA SCIENTIST ----------------

class DataScientist(Employee):
    def __init__(self, id, name, department, tool):
        super().__init__(id, name, department)
        self.tool = tool
    def get_role_details(self):
        return "Data Scientist - " + self.tool


# ---------------- MANAGER ----------------
class Manager(Employee):
    def __init__(self, id, name, department, team):
        super().__init__(id, name, department)
        self.team = team
    def get_role_details(self):
        return "Manager - Team Size " + str(self.team)


# ---------------- ITERATOR ----------------
class MyIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.employees):
            emp = self.employees[self.index]
            self.index = self.index + 1
            return emp
        else:
            raise StopIteration


# ---------------- GENERATOR ----------------
def task_generator(employees):
    for emp in employees:
        for task in emp.tasks:
            yield task


# ---------------- DECORATOR ----------------
@decorate
def process_tasks():
    for emp in employees:
        for task in emp.tasks:
            print(emp.name, ":", task)


# ---------------- MAIN PROGRAM ----------------
employees = []
while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Developer")
    print("2. Add Data Scientist")
    print("3. Add Manager")
    print("4. Add Task")
    print("5. Show Employees")
    print("6. Show Task Report")
    print("7. Process Tasks")
    print("8. Exit")
    choice = int(input("Enter choice: "))

    # Add Developer
    if choice == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        language = input("Enter Language: ")
        emp = Developer(id, name, department, language)
        employees.append(emp)
        print("Developer added.")

    # Add Data Scientist
    elif choice == 2:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        tool = input("Enter Tool: ")
        emp = DataScientist(id, name, department, tool)
        employees.append(emp)
        print("Data Scientist added.")

    # Add Manager
    elif choice == 3:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        team = int(input("Enter Team Size: "))
        emp = Manager(id, name, department, team)
        employees.append(emp)
        print("Manager added.")

    # Add Task
    elif choice == 4:
        id = int(input("Enter Employee ID: "))
        task = input("Enter Task: ")
        for emp in employees:
            if emp.id == id:
                emp.add_task(task)
                print("Task added.")
                break

    # Show Employees
    elif choice == 5:
        it = MyIterator(employees)
        try:
            while True:
                emp = next(it)
                print("\nID:", emp.id)
                print("Name:", emp.name)
                print("Department:", emp.department)
                print("Role:", emp.get_role_details())
                print("Tasks:", emp.tasks)
        except StopIteration:
            print("End of employees.")

    # Generator
    elif choice == 6:
        print("\n===== TASK REPORT =====")
        for task in task_generator(employees):
            print(task)

    # Decorator
    elif choice == 7:
        process_tasks()

    # Exit
    elif choice == 8:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")