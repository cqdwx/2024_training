# MySQL学习笔记
- **创建docker-compose.yml文件**
```yaml
version: '3'
services:
mysql:
image: mysql:latest
restart: always
environment:
MYSQL_ROOT_PASSWORD: your_password
MYSQL_DATABASE: mydatabase
MYSQL_USER: user
MYSQL_PASSWORD: password
ports:
- "3306:3306"
```
- **启动MySQL容器**
```bash
docker-compose up -d
```
- **连接MySQL容器**
```bash
docker exec -it [container_id] mysql -uuser -ppassword mydatabase
```
- **登录MySQL**
```bash
mysql -uuser -ppassword mydatabase
```
- **创建数据库**
```sql
CREATE DATABASE mydatabase;
```
- **选择数据库**
```sql
USE mydatabase;
```
- **创建表**
```sql 
CREATE TABLE mytable ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) );
```
- **做增删查改**
```sql
-- 插入数据
INSERT INTO mytable (name) VALUES ('Alice');
-- 查询数据
SELECT * FROM mytable;
-- 更新数据
UPDATE mytable SET name = 'Bob' WHERE id = 1;
-- 删除数据
DELETE FROM mytable WHERE id = 1;
```