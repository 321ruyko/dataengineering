class Vehicle:
    def __init__(self,maxspeed=10,mileage=20):
        self.max_speed=maxspeed
        self.mileage=mileage
class Bus(Vehicle):
    def __init__(self):
        pass
    def farecharge(self):
        return (50 * 100) + (50 * .1)
# class Car(Vehicle):
#     def __init__(self):
#         pass
#
#     def farecharge(self, cp):
#         return (cp * 100)

bus=Bus()
car=Car()
print("Bus farecharge",bus.farecharge())
# print("Bus farecharge",car.farecharge(10))

