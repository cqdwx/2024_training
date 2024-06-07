# Python学习 
- **Python环境**
  - 对于ubuntu24.04系统来说，系统本身自带python，无需额外安装python，而在windows系统中进行开发的话，则是需要安装python并配置相关环境才能够使用。
  - 对于编译器，我选择使用VScode进行开发，因为VScode支持许多扩展包，能够很好的支持我们的开发。
- **Python运行**
  - 对于python文件的运行，我们只需要在相关python文件的文件夹目录下进入终端直接运行即可。
- **Python基本语法**
  - Python使用缩进来表示代码块，通常是4个空格。
  - 语句末尾不需要分号。
- **Python数据类型**
  - 整数（int）、浮点数（float）、字符串（str）是Python中最常见的数据类型。
  - 列表（list）、元组（tuple）、集合（set）和字典（dict）是常见的数据结构。 
- **if语句**
```python
if condition:
    # do something
elif another_condition:
    # do something else
else:
    # do other things
```
- **for语句**
```python
for item in sequence:
    # do something with item
```
- **函数**
```python
def my_function(arg1, arg2):
    # do something
    return result
```
- **异常处理**
```python
try:
    # code that may raise an exception
except SomeException as e:
    # handle the exception
finally:
    # optional cleanup code
```
- **面向对象编程**
```python
class MyClass:
    def __init__(self, arg):
        self.attribute = arg
        
    def my_method(self):
        # do something
```
- **文件操作**
```python
with open('file.txt', 'r') as file:
    data = file.read()
    # process data
```
- **常用库**
  - Python有大量的标准库，包括用于各种目的的模块，如os、sys、math等。
  - 第三方库如NumPy、Pandas、Matplotlib等提供了丰富的功能。
