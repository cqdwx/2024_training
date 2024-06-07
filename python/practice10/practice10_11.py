import json

def get_favorite_number():
    favorite_number = input("请输入你喜欢的数字：")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
    return favorite_number

def display_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
            print(f"I know your favorite number! It's {favorite_number}.")
    except FileNotFoundError:
        favorite_number = get_favorite_number()
        print(f"Your favorite number {favorite_number} has been stored.")

display_favorite_number()
