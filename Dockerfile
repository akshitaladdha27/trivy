FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /usr/local/app
COPY app.py .
CMD ["python", "app.py"]