FROM python:3.11.2

RUN pip install --upgrade pip \
        && mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/Main.py