from django.contrib import admin
from django.urls import path
from works import views

urlpatterns = [
    path('catalog/', views.CatalogPage.as_view(), name='catalog'),
    path('catalog/add_service/', views.AddServiceCreateView.as_view(), name='add_service'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
]