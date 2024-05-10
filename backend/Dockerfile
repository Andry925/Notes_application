FROM python:3.10-slim

RUN pip install --upgrade pip

COPY ./requiremnts.txt .
RUN pip install -r requiremnts.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]