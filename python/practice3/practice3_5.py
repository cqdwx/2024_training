guests = ["张三", "李四", "王五"]
print(guests[1] + " 无法赴约。")
guests[1] = "赵六"
for guest in guests:
    print(guest + "，您好！欢迎您共进晚餐。")