try:
    with open('cats.txt') as file_object:
        cats = file_object.read()
    with open('dogs.txt') as file_object:
        dogs = file_object.read()
    print("猫的名字：\n" + cats)
    print("狗的名字：\n" + dogs)
except FileNotFoundError:
    pass  # 静默失败