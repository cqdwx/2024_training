# Docker学习笔记
- **启动MySQL容器**
```bash 
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -d mysql:latest
```
- **连接MySQL容器**
```bash 
docker exec -it mysql-container mysql -uroot -p 
```
- **创建数据库**
```sql CREATE DATABASE mydatabase; ```
- **创建表**
```sql 
USE mydatabase;
CREATE TABLE mytable ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) );
```
- **做增删查改**
```
-- 插入数据
INSERT INTO mytable (name) VALUES ('Alice');
```
```
-- 查询数据
SELECT * FROM mytable;
```
```
-- 更新数据
UPDATE mytable SET name = 'Bob' WHERE id = 1;
```
```
-- 删除数据
DELETE FROM mytable WHERE id = 1;
```
- **启动Redis容器**
```bash 
docker run --name redis-container -d redis:latest
```
- **连接Redis容器**
```bash 
docker exec -it redis-container redis-cli
```
- **做增删查改**
```bash
# 设置键值对
SET mykey "Hello"
# 获取键值对
GET mykey
# 删除键值对
DEL mykey
```
- Docker Compose是一个用于定义和运行多容器Docker应用程序的工具。通过一个单独的文件来配置应用的服务，然后使用一个命令即可创建并启动所有服务。
```yaml
version: '3'
services:
web:
image: nginx:latest
ports:
- "8080:80"
  db:
  image: mysql:latest
  environment:
  MYSQL_ROOT_PASSWORD: your_password
```
- **使用Docker Compose启动应用**
```bash
docker-compose up
```