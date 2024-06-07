# 创建多个表示宠物的字典
pet1 = {'animal_type': 'dog', 'owner': 'Alice'}
pet2 = {'animal_type': 'cat', 'owner': 'Bob'}
pet3 = {'animal_type': 'rabbit', 'owner': 'Charlie'}

# 将这些字典存储在一个名为 pets 的列表中
pets = [pet1, pet2, pet3]

# 遍历列表，并将有关每个宠物的所有信息打印出来
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()
