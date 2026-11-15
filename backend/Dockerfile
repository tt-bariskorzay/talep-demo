FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG SURUM=gelistirme
ENV SURUM=$SURUM
EXPOSE 8000
# Açılışta veritabanı tablolarını günceller, sonra uygulamayı başlatır
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn talep.wsgi -b 0.0.0.0:8000 -w 2"]
