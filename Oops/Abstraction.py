from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("mileage is 28kmph")
 
t=Tesla()
t.mileage()

s=Suzuki()
s.mileage()