while True:
    try:
        num1 = int(input("请输入第一个数："))
        num2 = int(input("请输入第二个数："))
        result = num1 + num2
        print("结果是：", result)
    except ValueError:
        print("输入错误，请输入数字。")
        continue
    else:
        break