FROM python:3.9.13-buster

WORKDIR /app

ADD . /app /app

COPY ./requirements.txt /etc

RUN pip install -r /etc/requirements.txt
RUN pip install --upgrade pip

EXPOSE 8080

ENV NAME World
ENV MYSQL_HOST mysql
ENV MYSQL_ROOT_PASSWORD EXAMPLE
ENV MYSQL_DATABASE TEST
ENV MYSQL_USER TEST
ENV MYSQL_PASSWORD TEST
ENV MONGO_HOST mongodb
ENV REDIS_HOST redis
ENV MEMCACHE_HOST "memcache:11211"

CMD ["python", "app.py"]
