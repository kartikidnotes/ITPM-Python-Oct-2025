from abc import ABC, abstractmethod


# -------------------- LOGIN MODULE --------------------
class Login:
    def __init__(self):
        self.__username = "user"
        self.__password = "1234"

    def validate(self):
        u = input("Enter Username: ")
        p = input("Enter Password: ")

        if u == self.__username and p == self.__password:
            print("Login Successful\n")
            return True
        else:
            print("Invalid Login\n")
            return False


# -------------------- CAB ABSTRACTION --------------------
class Cab(ABC):

    @abstractmethod
    def calculate_fare(self, km):
        pass


# -------------------- CAB TYPES --------------------
class Mini(Cab):
    def calculate_fare(self, km):
        return km * 10


class Sedan(Cab):
    def calculate_fare(self, km):
        return km * 15


class SUV(Cab):
    def calculate_fare(self, km):
        return km * 20


# -------------------- BOOKING MODULE --------------------
class Booking:
    def __init__(self, name):
        self.name = name

    def book(self):
        print("\nCab Types Available")
        print("1. Mini (₹10/km)")
        print("2. Sedan (₹15/km)")
        print("3. SUV (₹20/km)")

        try:
            choice = int(input("Choose Cab Type: "))
            km = int(input("Enter Distance (km): "))

            if km <= 0:
                print("Distance must be greater than 0\n")
                return

            if choice == 1:
                cab = Mini()
                cab_name = "Mini"
            elif choice == 2:
                cab = Sedan()
                cab_name = "Sedan"
            elif choice == 3:
                cab = SUV()
                cab_name = "SUV"
            else:
                print("Invalid Choice\n")
                return

            amount = cab.calculate_fare(km)

            print("\n----- BOOKING CONFIRMED -----")
            print("Customer Name:", self.name)
            print("Cab Type:", cab_name)
            print("Distance:", km, "km")
            print("Total Fare: ₹", amount)
            print("------------------------------\n")

        except ValueError:
            print("Please enter valid numeric input\n")


# -------------------- MAIN PROGRAM --------------------
def main():
    login = Login()

    if login.validate():
        name = input("Enter Customer Name: ")
        booking = Booking(name)

        while True:
            print("1. Book Cab")
            print("2. Exit")

            try:
                ch = int(input("Enter choice: "))

                if ch == 1:
                    booking.book()
                elif ch == 2:
                    print("Thank you for using Cab Booking System 🚖")
                    break
                else:
                    print("Invalid Option\n")

            except ValueError:
                print("Please enter valid number\n")


# # Run Program
# if __name__ == "__main__":
main()