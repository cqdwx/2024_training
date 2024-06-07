class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# 创建一个名为restaurant的实例
restaurant = Restaurant("The Great Pizza Place", "Italian")
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
