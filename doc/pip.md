
1. 生成依赖的文件， 方便在其他平台重建项目运行环境

pip freeze > requirements.txt

2. 安装依赖

pip install -r requirements.txt


3. 数据迁移	
python manage.py dumpdata myapp > myapp.json #到处的文件格式任意没有限制，推荐python

4. 数据导入

python manage.py loaddata myapp.json



5. 新建一个新的app

python manage.py  startapp appname

6. 生成迁移文件

python manage.py   makemigrations


7. 执行迁移

python manage.py  migrate

8. 开启服务

python manage.py  runserver


10. 查看 nigix 启动时间
ps -ef|grep  nginx


python manage.py collectstatic