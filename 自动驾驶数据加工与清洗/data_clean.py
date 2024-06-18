import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库连接
engine = create_engine('mysql://your_username:your_password@localhost/your_database')
Base = declarative_base()

# 定义数据表模型
class DataInfo(Base):
    __tablename__ = 'DataInfo'
    id = Column(Integer, primary_key=True)
    file_path = Column(String(255))
    text_content = Column(Text)
    file_size = Column(Integer)

# 创建数据表
Base.metadata.create_all(engine)

# 读取 data_info.json 文件
with open('data_info.json', 'r') as file:
    data_info = json.load(file)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 读取data_info.json文件中的文件路径，并将相关信息存储到数据库表中
for entry in data_info:
    file_path = os.path.abspath(entry.get("resource"))
    if file_path:
        new_data = DataInfo(file_path=file_path)
        if file_path.endswith(".txt"):
            with open(file_path, 'r') as text_file:
                text_content = text_file.read()
            new_data.text_content = text_content
        elif file_path.endswith(".bin"):
            file_size = os.path.getsize(file_path)
            new_data.file_size = file_size
        session.add(new_data)

# 提交更改并关闭会话
session.commit()
session.close()


