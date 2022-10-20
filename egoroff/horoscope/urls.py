from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<int:month>/<int:day>/', views.dayandmonth),
    path('type/', views.typeindex),
    path('type/<type>', views.elementindex, name='type_name'),
    path('<int:sign_zodiac>/', views.sign_by_num),
    path('<sign_zodiac>/', views.sign, name='horoscope_name'),
]
