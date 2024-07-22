class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
       return self.capacity - len(self.passengers)    

flight = Flight(3)       


people = ["Tozé", "Ron", "Kaka", "Toni"]

for person in people:
        if flight.add_passenger(person):
            print(f"Added {person} to flight with success")
        else:
            print(f"Not available seat for {person}")
