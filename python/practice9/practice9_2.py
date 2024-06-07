class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
# 创建三个餐馆实例并调用describe_restaurant方法
restaurant1 = Restaurant("La Belle Cuisine", "French")
restaurant2 = Restaurant("Sushi Haven", "Japanese")
restaurant3 = Restaurant("Spice Bazaar", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
