class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f'The restaurant is called {self.restaurant_name} and they serve {self.cuisine_type} cuisine')


    def open_restaurant(self):
        print("The restaurant is open!")


    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, add):
        self.number_served += add

restaurant = Restaurant("dos tacos", "mexican")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

restaurant_01 = Restaurant("Chakara", "Indian")
restaurant_02 = Restaurant("Mama", "Ethiopian")
restaurant_03 = Restaurant("brooklyn", "American")

restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()

print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(2)
print(restaurant.number_served)