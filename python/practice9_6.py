class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)

# 创建一个 IceCreamStand 实例
ice_cream_stand = IceCreamStand("The Sweet Scoop", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
