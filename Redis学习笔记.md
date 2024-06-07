# Redis学习笔记
- **创建docker-compose.yml文件**
```yaml
version: '3'
services:
  redis:
    image: redis:latest
    restart: always
    ports:
      - "6379:6379"
```
- **启动Redis容器**
```bash
docker-compose up -d
```
- **连接Redis容器**
```bash
docker exec -it [container_id] redis-cli
```
- **设置键值对**
```bash
SET mykey "Hello"
```
- **获取键值对**
```bash
GET mykey
```
- **删除键值对**
```bash
DEL mykey
```