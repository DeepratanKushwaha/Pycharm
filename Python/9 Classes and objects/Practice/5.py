# create class train which has methods to book ticket, get status and fare information of trains

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of train is {self.name}")
        print(f"{self.seats} seats are available")

    def fareInfo(self):
        print(f"Cost of fare is Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, this train is full!!")

    def cancelTicket(self, seat):
        pass


intercity = Train("Intercity Express: 14345", 100, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
