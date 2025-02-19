FROM python:3.10-slim-buster

WORKDIR /app

# Копируем requirements.txt (он в папке Generation)
COPY Generation/requirements.txt .

RUN pip install -r requirements.txt

# Копируем всё из корня в /app (попадёт и manage.py, и Generation/)
COPY . .  

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
