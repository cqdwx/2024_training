sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'ham', 'cheese']
finished_sandwiches = []
print("对不起，五香熏牛肉卖完了。")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("以下三明治已制作完成：")
for sandwich in finished_sandwiches:
    print(sandwich)
