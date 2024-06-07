# 练习 10.4
# 提示用户输入姓名，并将其写入文件 guest.txt
name = input("请输入您的名字: ")
with open('guest.txt', 'w') as file_object:
    file_object.write(name)

