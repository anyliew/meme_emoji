# Docker-compose  部署 meme-generator



## meme-generator

*✨ 表情包生成器，用于制作各种沙雕表情包 ✨*



## Docker-compose 部署过程



#### 拉取镜像

```bash
docker pull meetwq/meme-generator:main
```



### 创建Docker-compose文件以及内容

创建文件

```bash
vim /opt/meme/meme-generator.yaml
```

文件内容

```yaml
version: '3'
services:
  meme-generator:
    image: meetwq/meme-generator:main
    container_name: meme-generator
    restart: always
    ports:
      - "2233:2233"
    volumes:
    	#额外表情路径
      - <YOUR_DATA_DIR>:/data
    environment:
      - MEME_DIRS='["/data/memes"]'
      - MEME_DISABLED_LIST='[]'
      - GIF_MAX_SIZE=10.0
      - GIF_MAX_FRAMES=100
      - BAIDU_TRANS_APPID=<YOUR_BAIDU_TRANS_APPID>
      - BAIDU_TRANS_APIKEY=<YOUR_BAIDU_TRANS_APIKEY>
      - LOG_LEVEL=INFO
```

### 运行容器

```bash
docker-compose -f /opt/meme/meme-generator.yaml up -d
```

