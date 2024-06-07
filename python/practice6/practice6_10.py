# 修改练习 6.2 编写的程序，让每个人都可以有多个喜欢的数字
favorite_numbers = {
    'Alice': [7, 11, 23],
    'Bob': [3, 8, 17],
    'Charlie': [2, 9, 14]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are: {', '.join(map(str, numbers))}")
