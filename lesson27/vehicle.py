
class vehicle:
    
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

lambo = vehicle(350, 30)

print("the max speed of the lambo is", lambo.max_speed)
print("the mileage of the lambo is", lambo.mileage)

