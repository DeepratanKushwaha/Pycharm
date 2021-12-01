# create class employee and add salary and increment properties to it
# write method salaryafterincrement with a @property decorator with a setter which changes the value of increment
# based on the salary


class Employee:
    salary = 1000
    increment = 1.5

    @property
    def SalaryAfterIncrement(self):
        return self.salary * self.increment

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, sai):            # sai = salaryafterincerment
        self.increment = sai/self.salary


e = Employee()
print(e.increment)
print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement = 2000
print(e.SalaryAfterIncrement)
print(e.increment)
