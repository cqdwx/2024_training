# 作者：[你的姓名]
# 日期：[当前日期]
# 功能：这段代码使用Python的removesuffix()方法去除文件扩展名，并打印出不包含扩展名的文件名。

filename = 'python_notes.txt'

# 使用 removesuffix() 方法去除文件扩展名
filename_without_extension = filename.removesuffix('.txt')

# 打印不包含扩展名的文件名
print("文件名（不包含扩展名）:", filename_without_extension)
