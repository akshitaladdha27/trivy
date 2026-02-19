FROM python:3.13

WORKDIR /usr/local/app

COPY app.py .

CMD ["python", "app.py"]