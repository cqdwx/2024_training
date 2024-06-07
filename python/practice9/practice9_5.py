class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# 创建一个名为user的实例
user = User("John", "Doe", 30, "john.doe@example.com")

# 调用increment_login_attempts方法多次并打印属性login_attempts的值
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("Login attempts:", user.login_attempts)

# 调用reset_login_attempts方法并再次打印属性login_attempts的值
user.reset_login_attempts()
print("Login attempts:", user.login_attempts)
