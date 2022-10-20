from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import math


# Create your views here.


def get_rectangle_area(request, width, height):
    # s = width * height
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {s}')
    return render(request, '/geometry/rectangle.html')


def redirect_rectangle(request, width, height):
    redirect_url = reverse("rectangle", args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area(request, width):
    # s = width ** 2
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {s}')
    return render(request, 'geometry/square.html')


def redirect_square(request, width):
    redirect_url = reverse('square', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request, radius):
    # return HttpResponse(f'Площадь круга радиусом {radius} равна {math.pi * radius ** 2}')
    return render(request, 'geometry/circle.html')


def redirect_circle(request, radius):
    redirect_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirect_url)
