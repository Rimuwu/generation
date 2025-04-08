FROM python:3.10-slim-buster

WORKDIR /app

# Копируем requirements.txt (он в папке Generation)
COPY Generation/requirements.txt .

RUN pip install -r requirements.txt

# Копируем всё из корня в /app (попадёт и manage.py, и Generation/)
COPY . .  

ENV DJANGO_SUPERUSER_USERNAME=as1
ENV DJANGO_SUPERUSER_PASSWORD=1304

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
