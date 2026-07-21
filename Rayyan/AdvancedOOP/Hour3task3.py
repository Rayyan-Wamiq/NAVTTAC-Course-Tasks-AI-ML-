class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Phone:
    def __init__(self, capacity):
        self.battery = Battery(capacity)

phone = Phone(7000)
print(phone.battery.capacity)

###Task4###
#  1) Composition
#  2) Aggregation
#  3) Association
