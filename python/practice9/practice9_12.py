# admin_test.py

from admin import Admin

# 创建一个 Admin 实例并调用 show_privileges() 方法
admin = Admin("Alice", "Admin", 40, "alice.admin@example.com", ["can add post", "can delete post", "can ban user"])
admin.privileges.show_privileges()
