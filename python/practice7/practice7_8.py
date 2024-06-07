sandwich_orders = ['tuna', 'chicken', 'ham', 'cheese']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("以下三明治已制作完成：")
for sandwich in finished_sandwiches:
    print(sandwich)
