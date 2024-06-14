# 关于mysql数据库的增删改查，不仅仅只可以使用sqlachemy，也可以通过pymysql连接数据库后进行相关操作，从而达到增删改查的功能。

import pymysql

# 数据库连接信息
db_user = 'cq'
db_password = '123456'
db_host = 'localhost'
db_port = 3306
db_name = 'mydb'

# 创建数据库连接
connection = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_password,
                             database=db_name,
                             port=db_port,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 创建数据表
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table created successfully")

        # 插入数据
        insert_query = "INSERT INTO students (name, age) VALUES (%s, %s)"
        student_data = ('John', 25)
        cursor.execute(insert_query, student_data)
        connection.commit()
        print("Data inserted successfully")

        # 查询数据
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        records = cursor.fetchall()
        for row in records:
            print(f"ID: {row['id']}, Name: {row['name']}, Age: {row['age']}")

        # 更新数据
        update_query = "UPDATE students SET age = %s WHERE name = %s"
        new_age = 30
        student_name = 'John'
        cursor.execute(update_query, (new_age, student_name))
        connection.commit()
        print("Data updated successfully")

        # 删除数据
        delete_query = "DELETE FROM students WHERE name = %s"
        student_name = 'John'
        cursor.execute(delete_query, (student_name,))
        connection.commit()
        print("Data deleted successfully")

finally:
    connection.close()
    print("MySQL connection is closed")