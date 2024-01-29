class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeSorter:
    def __init__(self, employees):
        self.employees = employees

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif key == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif key == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")

    def print_sorted_data(self):
        for emp in self.employees:
            print(emp)


if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_sorter = EmployeeSorter(employees_data)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sorting_param = int(input("Enter your choice (1/2/3): "))
    employee_sorter.sort_employees(sorting_param)
    print("\nSorted Employee Data Will there be a merge conflict?:")
    employee_sorter.print_sorted_data()


