class Emp:

    def __init__(self,name,salary):
        '''Contrustor initialize while creating a object'''
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(self.salary)

rohan = Emp("rohan","3099")
print(rohan.name)
print(rohan.salary)

Farid = Emp("Farid","30399")
print(Farid.name)
print(Farid.salary)

rohan.getSalary()