# 练习 10.5
# 收集用户输入的名字并写入 guest_book.txt
with open('guest_book.txt', 'w') as file_object:
    while True:
        name = input("请输入您的名字（输入'q'退出）: ")
        if name == 'q':
            break
        file_object.write(name + "\n")