# build stage
FROM python:3 as base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# run stage
FROM python:3-alpine
WORKDIR /app
COPY --from=base /app/requirements.txt ./
COPY --from=base /root/.cache /root/.cache
RUN pip install -r requirements.txt && rm -rf /root/.cache
COPY info.py ./
ENTRYPOINT ["python3","info.py"]

