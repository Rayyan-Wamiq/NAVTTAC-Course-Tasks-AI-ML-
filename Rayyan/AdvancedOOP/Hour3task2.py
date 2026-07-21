class Wheel:
    def __init__(self, size):
        self.size = size

    def info(self):
        print(f"Wheel Size: {self.size}")

class Bicycle:
    def __init__(self, wheel):
        self.wheel = wheel

wheel = Wheel(17)

bike = Bicycle(wheel)
print(bike.wheel.size)

del bike

wheel.info()
