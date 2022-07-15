FROM python:3.9.13-buster

WORKDIR /app

ADD . /app

COPY ./requirements.txt /etc

RUN pip install --upgrade pip
RUN pip install -r /etc/requirements.txt

CMD ["python", "/app/codigo/app.py"]