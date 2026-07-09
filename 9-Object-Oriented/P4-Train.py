import random

class Train:
    def book_ticket(self, train_no, from_station, to_station):
        print(f"Ticket is booked with the train number {train_no} from station {from_station} to station {to_station}")
        
    def getstatus(self, train_no):
        print(f"Status of train number {train_no} is available")

    def fare(self, train_no, from_station, to_station):
        print(f"Ticket fare with the train number {train_no} from station {from_station} to station {to_station} is {random.randint(100, 5000)}")

t = Train()
t.book_ticket(12345, "Hathras", "Mathura")
t.getstatus(12345)
t.fare(12345, "Hathras", "Mathura")