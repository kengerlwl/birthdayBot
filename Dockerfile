# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装时区设置工具
RUN apt-get update && apt-get install -y tzdata

# 设置时区为上海（Asia/Shanghai）
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 安装cron和Supervisor
RUN apt-get install -y cron supervisor

# 添加cron定时任务文件
COPY cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob

# 将cron任务导入cron服务
RUN crontab /etc/cron.d/cronjob

# 创建Supervisor配置文件
COPY supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf

# 启动时通过Supervisor启动所有服务
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
