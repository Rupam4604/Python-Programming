class Employee:
    company = "asus"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name of the employee is {self.name}.salary is {self.salary}. bond is for {self.bond} years in {self.company}")


e1 = Employee(34000, "rupam", 4, "tesla")
print(e1.company)
print(Employee.company)
e1.get_info()



#object introspection
print(dir(e1))