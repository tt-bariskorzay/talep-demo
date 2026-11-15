from django.urls import path

from talepler import views

urlpatterns = [
    path("api/ortam/", views.ortam),
    path("api/talepler/", views.talepler),
]
