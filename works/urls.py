from django.contrib import admin
from django.urls import path
from works import views

urlpatterns = [
    path('catalog/', views.CatalogPage.as_view(), name='catalog'),
]