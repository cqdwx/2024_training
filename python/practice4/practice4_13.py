# 定义包含 5 种简单食品的元组
simple_foods = ('apple', 'banana', 'bread', 'cheese', 'salad')

# 打印出餐馆提供的 5 种食品
print("餐馆提供的食品有：")
for food in simple_foods:
    print(food)

# 尝试修改其中的一个元素
# 以下代码会导致错误：TypeError: 'tuple' object does not support item assignment
# simple_foods[0] = 'pear'

# 餐馆调整菜单，替换两种食品
simple_foods = ('orange', 'banana', 'bread', 'cheese', 'pasta')

# 打印出新的元组的每个元素
print("\n餐馆调整菜单后提供的食品有：")
for food in simple_foods:
    print(food)
