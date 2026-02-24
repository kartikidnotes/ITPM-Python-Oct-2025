from abc import ABC,abstractmethod
# from packagename import Abstrct Base Class, abstractmethod

class Payment(ABC):

    # @-- decorator 
    @abstractmethod
    def pay(self,amount):
        pass


#child 
class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid the {amount} using credit Card")
        # {} -- interpolation

class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI ")

c=CreditCard()
c.pay(2000)

u=UPI()
u.pay(4000)