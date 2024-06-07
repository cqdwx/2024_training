car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 更多条件测试
print("\n--- More Conditional Tests ---")

# 字符串相等和不等的条件测试
string1 = "hello"
string2 = "Hello"
print("\nIs 'hello' == 'Hello'? I predict False.")
print(string1 == string2)

print("\nIs 'hello' != 'Hello'? I predict True.")
print(string1 != string2)

# 使用lower()方法的条件测试
print("\nIs 'hello' == 'HELLO' after lower() method? I predict True.")
print(string1.lower() == string2.lower())

# 数值比较的条件测试
num1 = 10
num2 = 5
print("\nIs 10 > 5? I predict True.")
print(num1 > num2)

print("\nIs 10 <= 5? I predict False.")
print(num1 <= num2)

# 使用and和or关键字的条件测试
num3 = 15
print("\nIs 10 < 15 and 15 > 5? I predict True.")
print(num1 < num3 and num3 > num2)

# 测试特定的值是否在列表中
fruits = ['apple', 'banana', 'orange']
print("\nIs 'apple' in the fruits list? I predict True.")
print('apple' in fruits)

print("\nIs 'grape' not in the fruits list? I predict True.")
print('grape' not in fruits)