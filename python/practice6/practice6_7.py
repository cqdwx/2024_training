# 创建三个人的字典
person1 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 25,
    'city': 'New York'
}

person2 = {
    'first_name': 'Bob',
    'last_name': 'Johnson',
    'age': 30,
    'city': 'San Francisco'
}

person3 = {
    'first_name': 'Charlie',
    'last_name': 'Brown',
    'age': 28,
    'city': 'Los Angeles'
}

# 将这三个字典存储在一个名为 people 的列表中
people = [person1, person2, person3]

# 遍历列表，将每个人的所有信息打印出来
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()
