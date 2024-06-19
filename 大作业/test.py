import requests
# 定义要查询的图像文件名
image_name = "000000.jpg"

# 发送 GET 请求
response = requests.get(f"http://127.0.0.1:8000/search/?image_name={image_name}")

# 打印响应内容
print(response.json())