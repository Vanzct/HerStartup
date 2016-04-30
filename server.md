服务器列表
    47.90.19.96 (公), 10.24.186.7(内) 正式服务器
    =====================================================

    CPU-1核 内存：1G 网络：1Mbps 硬盘：40GB SSD
    已安装服务：git nginx python-pip

项目管理和维护
    安装命令：apt-get install | yum install
    服务管理命令：service 服务名 [start|stop|reload|configtest|status|force-reload|upgrade|restart|reopen_logs]


    连接服务器：ssh 用户名@ip
    查看端口占用：lsof -i:5000 端口被哪个进程占用

@她本营的小朋友们：

1. 登录服务器
ssh root@47.90.19.96

2.进入项目目录
cd /home/apps/her

3.加载环境执行
. venv/bin/activate

4.拉代码
git pull

5.查看服务进程
lsof -i:5000
出现以下内容
    uwsgi   13728 root    3u  IPv4 249428      0t0  TCP localhost:5000 (LISTEN)
    uwsgi   13731 root    3u  IPv4 249428      0t0  TCP localhost:5000 (LISTEN)
    uwsgi   13732 root    3u  IPv4 249428      0t0  TCP localhost:5000 (LISTEN)

13728 就是主进程ID

6.杀掉现在的服务
kill -9 13728  # 13728 是主进程ID

7.重新启动应用
uwsgi uwsgi.ini

如果py文件没有改变只需要执行前4个步骤就可以