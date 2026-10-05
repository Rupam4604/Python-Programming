class employee:
    company = "hp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#  Instance method

    def print_info(self):
        info = f"the name of the employee is {self.name} and salary is {self.salary}"
        print(info)


#  Static method

    @staticmethod
    def sum(a, b):
        return a+b

#  class method

    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
        

e1 = employee("rupam", 5000)
e2 = employee("sayanti", 70000)

print(employee.company)
#print(employee.name)      # this wll thorw an error

e1.print_info()
e2.print_info()

print(e1.sum(5, 3))

print(employee.company)
e1.change_company("msi")
print(employee.company
      )