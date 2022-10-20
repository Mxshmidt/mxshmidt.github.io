from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days = {
    'monday': 'We go to work',
    'tuesday': 'We go to worship Gods',
    'wednesday': 'We go into the woods',
    'thursday': 'We go to bath with boys',
    'friday': 'We go drink and have fun',
    'saturday': 'We will take lessons from universe',
    'sunday': 'We go to the beach'
}


def intro(request):
    return render(request, 'week_days/greeting.html')

def plan_on_that_day(request, someday: str):
    plan = days.get(someday)
    if plan:
        return HttpResponse(plan)
    else:
        return HttpResponseNotFound(f'There is no such week day - {someday}')


def someday(request, someday: int):
    weekdays = list(days)
    if 7 >= someday > 0:
        day = weekdays[someday - 1]
        redirect_url = reverse("week_plan", args=(day,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {someday}')
# Create your views here.
