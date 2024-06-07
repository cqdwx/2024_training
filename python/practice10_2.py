# 练习 10.2
# 替换文件中的 Python 为 C
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

modified_lines = []
for line in lines:
    modified_lines.append(line.replace('Python', 'C'))

for modified_line in modified_lines:
    print(modified_line.rstrip())