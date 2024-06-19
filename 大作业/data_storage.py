import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Text

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
class DataInfo(Base):
    __tablename__ = 'data_info'
    id = Column(Integer, primary_key=True)
    image_path = Column(String(255))  # 为字段指定长度
    pointcloud_path = Column(String(255))  # 为字段指定长度
    label_lidar_std_content = Column(Text)
    calib_lidar_to_camera_content = Column(Text)
    calib_camera_intrinsic_content = Column(Text)

# 在数据库中创建表
Base.metadata.create_all(engine)

# 读取data_info.json文件
with open('./Data_example/data_info.json', 'r') as file:
    data = json.load(file)

# 将数据存储到MySQL数据库
Session = sessionmaker(bind=engine)
session = Session()
try:
    for item in data:
        # 读取相应路径中的JSON文件内容
        with open('./Data_example/' + item['label_lidar_std_path'], 'r', encoding='utf-8') as label_file:
            label_content = label_file.read()
        with open('./Data_example/' + item['calib_lidar_to_camera_path'], 'r', encoding='utf-8') as calib_lidar_file:
            calib_lidar_content = calib_lidar_file.read()
        with open('./Data_example/' + item['calib_camera_intrinsic_path'], 'r', encoding='utf-8') as calib_camera_file:
            calib_camera_content = calib_camera_file.read()

        new_data = DataInfo(
            image_path=item['image_path'],
            pointcloud_path=item['pointcloud_path'],
            label_lidar_std_content=label_content,
            calib_lidar_to_camera_content=calib_lidar_content,
            calib_camera_intrinsic_content=calib_camera_content
        )
        session.add(new_data)

    # 提交更改
    session.commit()
    print("数据存储成功")
except Exception as e:
    print(f"数据存储失败: {e}")
finally:
    # 关闭连接
    session.close()