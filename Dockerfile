FROM python:3.13-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# Add src folder to PYTHONPATH so imports work
ENV PYTHONPATH=/app/src

EXPOSE 8080
CMD ["python3", "app.py"]