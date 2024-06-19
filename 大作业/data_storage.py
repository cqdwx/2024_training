import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

# 定义数据表模型
class DataInfo(Base):
    __tablename__ = 'data_info'
    id = Column(Integer, primary_key=True)
    image_path = Column(String(255))
    pointcloud_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    calib_lidar_to_camera_path = Column(String(255))
    calib_camera_intrinsic_path = Column(String(255))


Base.metadata.create_all(engine)

# 读取data_info.json文件
with open('./Data_example/data_info.json', 'r') as file:
    data = json.load(file)

# 将数据存储到MySQL数据库
Session = sessionmaker(bind=engine)
session = Session()
try:
    for item in data:
        new_data = DataInfo(
            image_path=item['image_path'],
            pointcloud_path=item['pointcloud_path'],
            label_lidar_std_path=item['label_lidar_std_path'],
            calib_lidar_to_camera_path=item['calib_lidar_to_camera_path'],
            calib_camera_intrinsic_path=item['calib_camera_intrinsic_path']
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