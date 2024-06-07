my_list = [1, 2, 3, 4, 5]

try:
    # 尝试访问超出索引范围的元素，引发索引错误
    print(my_list[10])
except IndexError:
    print("引发了索引错误！")

print("程序继续执行...")
