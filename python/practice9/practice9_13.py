import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

# 创建一个6面的骰子并掷10次
print("Rolling a 6-sided die 10 times:")
d6 = Die()
for _ in range(10):
    d6.roll_die()

# 创建一个10面的骰子并掷10次
print("\nRolling a 10-sided die 10 times:")
d10 = Die(sides=10)
for _ in range(10):
    d10.roll_die()

# 创建一个20面的骰子并掷10次
print("\nRolling a 20-sided die 10 times:")
d20 = Die(sides=20)
for _ in range(10):
    d20.roll_die()
