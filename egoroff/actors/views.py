from django.shortcuts import render


def reaves(request):
    content = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Мой личный штат Айдахо'
    }
    return render(request, 'actors/keanu.html', context=content)


# Create your views here.


def guiness(request):
    content = {
        'power_man': 'Narve Laeret',
        'bar_name': "Bob's BBQ & Grill",
        'count_needle': 1790
    }
    return render(request, 'actors/guiness.html', context=content)
