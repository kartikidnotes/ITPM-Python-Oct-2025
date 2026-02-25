from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def cal_salary(self):
        pass

class FullTimeEmp(Employee):
    def __init__(self,monthly_sal):
        self.monthly_sal=monthly_sal

    def cal_salary(self):
        return self.monthly_sal
    

class FreelancerEmp(Employee):
    def __init__(self,hours,rate):
        self.hours=hours
        self.rate=rate

    def cal_salary(self):
        return self.hours*self.rate
    

e1=FullTimeEmp(50000)
print("Full TIme Employee Has Salaary :: ",e1.cal_salary())

e2=FreelancerEmp(5,1000)
print("Freelancer Employee Has Salaary calculated :: ",e2.cal_salary())
