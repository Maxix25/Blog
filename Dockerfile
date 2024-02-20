FROM python:3.11-alpine

ENV TIME_ZONE='America/Santiago'
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]