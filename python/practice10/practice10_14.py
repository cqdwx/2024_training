import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("请输入你的用户名：")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct_user = input(f"你是 {username} 吗？(yes/no): ")
        if correct_user.lower() == 'no':
            username = get_new_username()
    else:
        username = get_new_username()
    print(f"欢迎回来，{username}！")

greet_user()
