# First Flask Web Application

----

根据flask入门手册，学习并实践了flask 入门学习小程序，从这个小程序初步熟悉并了解flask框架，以及一个web程序的整体架构以及如何一步步编写一套web。


### 快速部署

#### CentOS

安装python3.7
```bash
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel epel-release -y
yum -y install python-pip wget  -y
#下载
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
#解压
tar -zxvf Python-3.7.0.tgz
cd Python-3.7.0
#配置
./configure prefix=/usr/local/python3
#编译安装
make && make install
#添加python3的软链接
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3.7
#添加 pip3 的软链接
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3.7
#测试是否安装成功了
python3.7 -V
```

### web程序部署
```bash
pip install pipenv
cd /opt
git clone https://github.com/xiaoyunjie/watchlist.git
cd watchlist
pipenv --python 3.7 install 
pipenv shell 
pipenv install flask  flask-login  flask-sqlalchemy python-dotenv
```

### 程序启动
```bash
pipenv shell
flask run
```
