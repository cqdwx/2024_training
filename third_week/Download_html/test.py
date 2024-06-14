# 正常获取HTML数据
import requests

# 发起GET请求获取HTML数据
response = requests.get('https://www.baidu.com')

# 检查请求是否成功
if response.status_code == 200:
    # 输出HTML数据
    print(response.text)
else:
    print("Failed to retrieve HTML data")