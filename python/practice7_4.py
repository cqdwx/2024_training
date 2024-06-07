while True:
    ingredient = input("请输入比萨配料（输入'quit'结束）：")
    if ingredient != 'quit':
        print(f"要在比萨中添加{ingredient}。")
    else:
        break
