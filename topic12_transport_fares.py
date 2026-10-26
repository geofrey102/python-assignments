class Vehicle:
    def calculateFare(self, distance):
        pass

class Bus(Vehicle):
    def calculateFare(self, distance):
        return distance * 50

class Taxi(Vehicle):
    def calculateFare(self, distance):
        return distance * 100

bus = Bus()
taxi = Taxi()

print(f"Bus Fare: KSh {bus.calculateFare(10):,.2f}")
print(f"Taxi Fare: KSh {taxi.calculateFare(10):,.2f}")

