# 多线程获取html数据并输出html信息
import requests
import threading
import queue

# 定义一个函数，用于下载网页的HTML数据
def download_html(url, q):
    response = requests.get(url)
    if response.status_code == 200:
        html_data = response.text
        q.put((url, html_data))  # 将URL和HTML数据放入队列
    else:
        q.put((url, "Failed to download HTML"))

# 要下载的网页列表
urls = ['https://www.baidu.com', 'https://www.firefox.com', 'https://www.microsoft.com']

# 创建队列
q = queue.Queue()

# 创建并启动线程
threads = []
for url in urls:
    thread = threading.Thread(target=download_html, args=(url, q))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 从队列中获取HTML数据并输出
while not q.empty():
    url, html_data = q.get()
    print(f"HTML data from {url}:")
    print(html_data)
    print("\n")

print("All downloads are completed")