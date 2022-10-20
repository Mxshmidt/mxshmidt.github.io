from django.urls import path
from . import views


urlpatterns = [
    path('keanu', views.reaves),
    path('guiness', views.guiness)
]
