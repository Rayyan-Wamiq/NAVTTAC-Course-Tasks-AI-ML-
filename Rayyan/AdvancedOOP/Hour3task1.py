class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, name):
        self.name = name

    def Drive(self, driver):
        print(f"{driver.name} is driving {self.name}.") 

driver = Driver("Rayyan")
car1 = Car("Toyota")
car2 = Car("Honda")

car1.Drive(driver)
car2.Drive(driver)