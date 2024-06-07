while True:
    age = input("请输入观众的年龄（输入'quit'结束）：")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("观众免费入场。")
    elif age <= 12:
        print("观众需要支付10美元。")
    else:
        print("观众需要支付15美元。")
