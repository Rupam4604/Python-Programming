# reate a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .
# Use @salary.setter to prevent setting negative values (print a warning
# instead).
# Create an object and test by setting positive and negative salaries


class empolyee:
    def __init__(self, salary):
        self._salary = salary
       

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if(value<0):
            print("piz set a proper salary, salaery cannot be negetive")
        else:
            self._salary = value


e = empolyee(50000)
e.salary = -5
print(e.salary)


