# 练习 10.3
# 删除临时变量，简化代码
with open('learning_python.txt') as file_object:
    for line in file_object.read().splitlines():
        print(line)