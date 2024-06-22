import requests
import zipfile
import io

# 下载文件
url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16213766573531136.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-18T06%3A39%3A49Z%2F604800%2F%2F603bb7f37c5745708675d3ade5c4e57f80fcdad198d5ebc34b8a63787fd835d2'
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# 解压文件
zip_file.extractall('../Data_example/')
zip_file.close()