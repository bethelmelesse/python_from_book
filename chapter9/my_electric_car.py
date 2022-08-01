from car2 import ElectricCar
print(" ")

my_tesla = ElectricCar('tesela', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print(" ") 