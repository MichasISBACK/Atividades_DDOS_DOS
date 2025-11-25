FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask psutil

EXPOSE 8000

CMD ["python", "app.py"]
