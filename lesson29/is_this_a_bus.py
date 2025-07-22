
class vehicles:

    def __init__(self, name, maximum_speed, mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage


class bus(vehicles):
    pass

school_bus = bus("school bus", 200, 20)
print("vehicle name:- ", school_bus.name, "speed:- ", school_bus.maximum_speed, "mileage:- ", school_bus.mileage)


        