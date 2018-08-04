FROM python:3-alpine
WORKDIR /app
COPY crawled_urls.txt ./
COPY filter_tool.py ./
ENTRYPOINT ["python3","filter_tool.py"]



