"""Talep uygulamasının ayarları.

Veritabanı ve ortam bilgisi ortam değişkenlerinden okunur. POSTGRES_HOST
tanımlı değilse (ör. testlerde) SQLite kullanılır.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "yalnizca-demo-icin")
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "talepler",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "talep.urls"
WSGI_APPLICATION = "talep.wsgi.application"

if os.environ.get("POSTGRES_HOST"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ["POSTGRES_HOST"],
            "NAME": os.environ.get("POSTGRES_DB", "talep"),
            "USER": os.environ.get("POSTGRES_USER", "talep"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

LANGUAGE_CODE = "tr"
TIME_ZONE = "Europe/Istanbul"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Ekranda gösterilen ortam adı ve sürüm (kurulumda verilir)
ORTAM = os.environ.get("ORTAM", "yerel")
SURUM = os.environ.get("SURUM", "gelistirme")
