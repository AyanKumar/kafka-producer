FROM python:3.6-slim


RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY app.py /app/app.py
COPY flaskapi-startup.sh /app/startup.sh
COPY flaskapi-uwsgi.ini /app/uwsgi.ini

COPY flaskapi-nginx.conf /etc/nginx

RUN chmod +x ./startup.sh

EXPOSE 80

CMD [ "./startup.sh" ]