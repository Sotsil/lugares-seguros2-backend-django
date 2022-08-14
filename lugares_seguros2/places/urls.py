from django.urls import path
from places import views


urlpatterns = [
    path('', views.PlaceView.as_view()),
    path('<int:id>', views.PlaceSingleView.as_view())
]