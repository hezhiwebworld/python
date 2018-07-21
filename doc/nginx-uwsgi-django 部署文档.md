
1. nginx 安装
sudo apt-get update
apt install  nginx


2. uwsgi 安装
pip3 install uwsgi


> 这里需要注意一点 pip 安装的uwsgi 里面内置的python 是python2.7
如果需要python3, 那么请安装pip3

3. 修改nginx.conf 文件， 配置server

4.  在应用的根目录 启动应用

nohup uwsgi --socket :8001 --module server.wsgi &

> socket 表示nginx 与uwsgi通讯的端口










