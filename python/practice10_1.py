# 练习 10.1
# 写入 Python 学习笔记到文件 learning_python.txt
with open('learning_python.txt', 'w') as file_object:
    file_object.write("In Python you can define variables and assign values to them.\n")
    file_object.write("In Python you can use loops like for and while to iterate over data.\n")
    file_object.write("In Python you can create functions to encapsulate reusable blocks of code.\n")

# 读取并打印文件内容两次
with open('learning_python.txt') as file_object:
    # 第一次打印，读取整个文件
    contents = file_object.read()
    print(contents)

    # 第二次打印，逐行读取
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())




