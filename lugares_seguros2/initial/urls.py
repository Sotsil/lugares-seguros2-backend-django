from django.urls import path

from initial import views

urlpatterns = [
    path('', views.HelloDrF.as_view(), name = 'index')
] 