from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro),
    path('<int:someday>/', views.someday),
    path('<str:someday>/', views.plan_on_that_day, name='week_plan')
]
