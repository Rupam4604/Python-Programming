class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name of the employee is {self.name}.salary is {self.salary}. bond is for {self.bond} years")


e1 = Employee(34000, "rupam", 4)

e1.get_info()