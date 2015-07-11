class Vehicle(object):
    def __init__(self, name, wheels, engine):
        self.name = name
        self.wheels = wheels
        self.engine = engine

    def number_of_wheels(self):
        return self.wheels

    def engine_type(self):
        return self.engine

class Car(Vehicle):
    def __init__(self, name, wheels, engine):
        super(Car, self).__init__(name, wheels, engine)


class Truck(Vehicle):
    def __init__(self, name, wheels, engine):
        super(Truck, self).__init__(name, wheels, engine)










