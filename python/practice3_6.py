guests = ["张三", "李四", "王五"]
print("我找到了一张更大的餐桌！")
guests.insert(0, "钱二")
guests.insert(2, "孙七")
guests.append("周八")
for guest in guests:
    print(guest + "，您好！欢迎您共进晚餐。")