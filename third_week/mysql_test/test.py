from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库连接信息
db_user = 'cq'
db_password = '123456'
db_host = 'localhost'
db_port = '3306'
db_name = 'mydb'

# 创建数据库引擎
db_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_url, echo=True)

# 创建基类
Base = declarative_base()

# 定义数据模型类
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 创建新学生
new_student = Student(name='John', age=25)

# 添加到会话
session.add(new_student)

# 提交事务
session.commit()

# 查询所有学生
students = session.query(Student).all()

# 打印学生信息
for student in students:
    print(f'ID: {student.id}, Name: {student.name}, Age: {student.age}')

# 查询要更新的学生
student = session.query(Student).filter_by(name='John').first()

# 更新年龄
student.age = 30

# 提交事务
session.commit()

# 查询要删除的学生
student = session.query(Student).filter_by(name='John').first()

# 从会话中删除学生
session.delete(student)

# 提交事务
session.commit()