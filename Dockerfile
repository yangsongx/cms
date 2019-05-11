FROM ubuntu:18.04

COPY ubuntu.18.04.sourcelist  /etc/apt/sources.list
COPY mycms /opt/mytest

RUN apt-get update
RUN apt-get install -y python3.6 python3-pip nginx
RUN apt-get install -y python3-dev libmysqlclient-dev supervisor

RUN ln -fs /usr/bin/python3.6 /usr/bin/python

# Ubuntu locale setting is different with CentOS
#RUN cp /usr/share/zoneinfo/PRC /etc/localtime

RUN mkdir -p /root/.pip/
RUN mkdir /opt/log


RUN echo '[global]' >/root/.pip/pip.conf
RUN echo 'index-url = http://pypi.douban.com/simple' >>/root/.pip/pip.conf

RUN pip3 install --trusted-host pypi.douban.com django==2.1.7
RUN pip3 install --trusted-host pypi.douban.com requests
RUN pip3 install --trusted-host pypi.douban.com ConcurrentLogHandler
RUN pip3 install --trusted-host pypi.douban.com oauthlib
RUN pip3 install --trusted-host pypi.douban.com django-cors-headers
RUN pip3 install --trusted-host pypi.douban.com boto3
RUN pip3 install --trusted-host pypi.douban.com djangorestframework
RUN pip3 install --trusted-host pypi.douban.com django-rest-swagger
RUN pip3 install --trusted-host pypi.douban.com gunicorn gevent
RUN pip3 install --trusted-host pypi.douban.com AWSIoTPythonSDK
RUN pip3 install --trusted-host pypi.douban.com pytz
RUN pip3 install --trusted-host pypi.douban.com APScheduler==2.1.2
RUN pip3 install --trusted-host pypi.douban.com schedule==0.5.0
RUN pip3 install --trusted-host pypi.douban.com mysqlclient
RUN pip3 install --trusted-host pypi.douban.com python3-memcached
RUN pip3 install --trusted-host pypi.douban.com django-redis


COPY conf.nginx /etc/nginx/sites-available/ftest
COPY conf.supervisord /etc/supervisor/conf.d/ftest.conf

RUN cd /etc/nginx/sites-enabled \
    && ln -s /etc/nginx/sites-available/ftest .
RUN unlink /etc/nginx/sites-enabled/default

# below try to solve the supervisor-Python2 and Django-Python3 issue...
RUN sed -i "1 i\\#\!\/usr\/bin\/python2\.7" /usr/bin/supervisord
RUN sed -i "1 i\\#\!\/usr\/bin\/python2\.7" /usr/bin/supervisorctl

#CMD ["/usr/bin/tail", "--retry", "-f", "/tmp/not.existed"]
CMD ["/usr/bin/supervisord", "-n"]
