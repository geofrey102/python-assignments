class Vehicle:
    def __init__(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    def displayVehicle(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)

class Bus(Vehicle):
    def __init__(self, registration_number, model, passenger_capacity):
        super().__init__(registration_number, model)
        self.passenger_capacity = passenger_capacity

    def displayBus(self):
        self.displayVehicle()
        print("Passenger Capacity:", self.passenger_capacity)

bus = Bus("KDA123A", "Isuzu", 45)
bus.displayBus()
