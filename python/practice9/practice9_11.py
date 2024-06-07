# admin_test.py

from user import Admin

# 创建一个 Admin 实例
admin = Admin("Alice", "Admin", 40, "alice.admin@example.com", ["can add post", "can delete post", "can ban user"])
admin.privileges.show_privileges()
