from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Optional


# 创建 FastAPI 应用
app = FastAPI()

# 创建数据库引擎
db_user = 'cq'
db_password = '123456'
db_host = 'localhost'
db_port = '3306'
db_name = 'mydb'
db_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_url, echo=True)

# 创建基类
Base = declarative_base()

# 定义数据模型
class DataInfo(Base):
    __tablename__ = 'data_info'
    id = Column(Integer, primary_key=True)
    image_path = Column(String(255))
    pointcloud_path = Column(String(255))
    label_lidar_std_content = Column(Text)
    calib_lidar_to_camera_content = Column(Text)
    calib_camera_intrinsic_content = Column(Text)

# 配置静态文件目录
app.mount("/images", StaticFiles(directory="/home/cq/2024_training/Data_example/image"), name="images")


# 定义查询输入模型
class ImageQuery(BaseModel):
    image_name: str


# 定义返回结果模型
class ImageResponse(BaseModel):
    image_path: str
    pointcloud_path: str
    label_lidar_std_content: str
    calib_lidar_to_camera_content: str
    calib_camera_intrinsic_content: str
    image_url: Optional[str]  # 新增字段用于存储图像的本地HTTP地址

# 定义路由
@app.get("/search/")
async def search_image(image_name: str):
    # 连接数据库
    Session = sessionmaker(bind=engine)
    session = Session()

    # 查询数据
    data = session.query(DataInfo).filter(DataInfo.image_path == f"image/{image_name}").first()

    # 构造返回数据
    if data:
        result = {
            "image_path": data.image_path,
            "pointcloud_path": data.pointcloud_path,
            "label_lidar_std_content": data.label_lidar_std_content,
            "calib_lidar_to_camera_content": data.calib_lidar_to_camera_content,
            "calib_camera_intrinsic_content": data.calib_camera_intrinsic_content,
            "image_url": f"http://127.0.0.1:8000/images/{image_name}"  # 设置图像的本地HTTP地址
        }
    else:
        result = {"message": "Image not found"}

    # 关闭连接
    session.close()

    return result


