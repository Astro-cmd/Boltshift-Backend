FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./db/scripts/backup.sh ./db/scripts/restore.sh

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
