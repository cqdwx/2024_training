import json

def get_user_info():
    user_info = {}
    user_info['username'] = input("请输入你的用户名：")
    user_info['age'] = input("请输入你的年龄：")
    user_info['location'] = input("请输入你的地点：")
    
    filename = 'user_info.json'
    with open(filename, 'w') as file_object:
        json.dump(user_info, file_object)
    return user_info

def display_user_info():
    filename = 'user_info.json'
    try:
        with open(filename) as file_object:
            user_info = json.load(file_object)
            print(f"程序记住了关于你的信息：\n{user_info}")
    except FileNotFoundError:
        user_info = get_user_info()
        print("你的个人信息已存储。")

display_user_info()
