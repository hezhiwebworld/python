要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

WSGI是一种Web服务器网关接口。它是一个Web服务器（如nginx，uWSGI等服务器）与web应用（如用Flask框架写的程序）通信的一种规范。
uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。
uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，它与WSGI相比是两样东西。




启动服务器
sudo /etc/init.d/nginx start
service nginx restart



uwsgi  --socket :8001 --ini /home/scripts/uwsgi.ini

cd   /home/python/django/server

uwsgi --socket :8001 --module server.wsgi

cd /home/python/django/server



nohup uwsgi --socket :8001 --module server.wsgi &