# 一个带有空白字符的人名
person_name = "\t\n  John Doe  \n\t"

# 打印原始姓名及其开头和末尾的空白
print("原始姓名:", repr(person_name))
print("姓名开头的空白:", repr(person_name.lstrip()))
print("姓名末尾的空白:", repr(person_name.rstrip()))
print("姓名两端的空白:", repr(person_name.strip()))
