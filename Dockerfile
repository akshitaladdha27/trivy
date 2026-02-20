FROM python:3.12-slim

WORKDIR /trivy

COPY requirements.txt .
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]