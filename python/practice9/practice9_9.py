class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# 创建一辆电动汽车并调用 get_range() 方法
my_electric_car = ElectricCar("Tesla", "Model S", 2024)
print("Initial range:", my_electric_car.battery.get_range())

# 升级电池并再次调用 get_range() 方法
my_electric_car.battery.upgrade_battery()
print("Upgraded range:", my_electric_car.battery.get_range())
