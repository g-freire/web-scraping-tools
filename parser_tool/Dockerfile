# build stage
FROM python:3.6.3-alpine3.6@sha256:aba3798848cd840e9d06f04e1dca81c82677e72e69ad9b2240a46c6754e56eab as base
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
ENV TERM xterm
RUN apk add --no-cache --virtual build-dependencies make gcc \
    g++ libxml2-dev libxslt-dev libffi-dev python3-dev 
RUN pip install -r requirements.txt 

COPY data/8804.txt /app/data/
COPY helper_functions.py /app/
COPY parser.py /app/

ENTRYPOINT ["python3","parser.py"]

