from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, marka, model, yil, tezlik):
        self._marka = marka
        self._model = model
        self._yil = yil
        self._tezlik = tezlik

    @property
    def tezlik(self):
        return self._tezlik

    @tezlik.setter
    def tezlik(self, value):
        if value >= 0:
            self._tezlik = value
        else:
            self._tezlik = 0

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"{self._marka} {self._model} | {self._yil} | Tezlik: {self.tezlik}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._marka}', '{self._model}', {self._yil}, {self.tezlik})"

    def __bool__(self):
        return self.tezlik > 0

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.tezlik == other.tezlik
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.tezlik > other.tezlik

    def __ge__(self, other):
        return self.tezlik >= other.tezlik

    def __lt__(self, other):
        return self.tezlik < other.tezlik

    def __le__(self, other):
        return self.tezlik <= other.tezlik


class Car(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} avtomobili ishga tushdi")

    def move(self):
        print("Mashina yo'lda harakatlanmoqda")


class Motorcycle(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} mototsikli ishga tushdi")

    def move(self):
        print("Mototsikl yo'lda harakatlanmoqda")


class Truck(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} yuk mashinasi ishga tushdi")

    def move(self):
        print("Yuk mashinasi yo'lda harakatlanmoqda")


car = Car("Chevrolet", "Malibu", 2023, 120)
motorcycle = Motorcycle("Honda", "CBR", 2022, 100)
truck = Truck("MAN", "TGX", 2021, 80)


vehicles = [car, motorcycle, truck]

for vehicle in vehicles:
    print(vehicle)
    vehicle.start()
    vehicle.move()
    print()


print(bool(car))

print(car == motorcycle)

print(car != truck)

print(car > motorcycle)

print(truck <= car)

print(repr(car))