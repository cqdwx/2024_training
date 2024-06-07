class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_number):
        self.number_served += additional_number

# 创建一个名为restaurant的实例
restaurant = Restaurant("The Great Pizza Place", "Italian")
print("Number served:", restaurant.number_served)

# 修改就餐人数并再次打印
restaurant.set_number_served(50)
print("Number served:", restaurant.number_served)

# 增加就餐人数并再次打印
restaurant.increment_number_served(30)
print("Number served:", restaurant.number_served)
