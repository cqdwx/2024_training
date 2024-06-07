class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

# 创建多个用户实例并调用方法
user1 = User("John", "Doe", 30, "john.doe@example.com")
user2 = User("Jane", "Smith", 25, "jane.smith@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
