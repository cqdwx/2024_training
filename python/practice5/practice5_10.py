current_users = ['john', 'emma', 'sophia', 'oliver', 'james']
new_users = ['James', 'Sophia', 'Liam', 'Ava', 'Mia']

# 将 current_users 列表中的所有用户名转换为小写形式
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a different username.")
    else:
        print(f"The username '{new_user}' is available.")
