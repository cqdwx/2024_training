import redis

# 创建Redis连接
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# 设置键值对
r.set('name', 'Alice')

# 获取值
name = r.get('name')
print(name)  # 输出：b'Alice'

# 删除键
r.delete('name')

# 检查是否存在
exists = r.exists('name')
print(exists)  # 输出：0

# 哈希表操作
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', 'age', 25)

user_info = r.hgetall('user:1')
print(user_info)  # 输出：{b'name': b'Alice', b'age': b'25'}