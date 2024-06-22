import json
import pandas as pd

# 读取JSON数据
with open('./Data_example/data_info.json', 'r') as file:
    data = json.load(file)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)

# 检查数据格式
expected_columns = ['image_path', 'image_timestamp', 'pointcloud_path', 'point_cloud_stamp', 'calib_camera_intrinsic_path', 'calib_lidar_to_camera_path', 'label_camera_std_path', 'label_lidar_std_path']
missing_columns = [col for col in expected_columns if col not in df.columns]
if missing_columns:
    print(f'Missing columns: {missing_columns}')

# 处理缺失值
df = df.dropna()

# 验证数据有效性
df['image_timestamp'] = pd.to_datetime(df['image_timestamp'], unit='ns')
df['point_cloud_stamp'] = pd.to_datetime(df['point_cloud_stamp'], unit='ns')

# 数据转换
df['image_timestamp'] = pd.to_datetime(df['image_timestamp'], unit='ns')
df['point_cloud_stamp'] = pd.to_datetime(df['point_cloud_stamp'], unit='ns')

# 将清洗后的数据保存到新的JSON文件
df.to_json('./Data_example/cleaned_data.json', orient='records')