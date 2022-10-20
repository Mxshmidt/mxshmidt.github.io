from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}

typedict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

daysinmonthdict = {
    1: 31,
    2: 60,
    3: 91,
    4: 120,
    5: 152,
    6: 182,
    7: 213,
    8: 244,
    9: 274,
    10: 305,
    11: 335,
    12: 366
}

daysandsignsdict = (
    ('aries', 111),
    ('taurus', 142),
    ('gemini', 173),
    ('cancer', 204),
    ('leo', 234),
    ('virgo', 267),
    ('libra', 297),
    ('scorpio', 327),
    ('sagittarius', 357),
    ('capricorn', 365),
    ('capricorn', 20),
    ('aquarius', 50),
    ('pisces', 80)
)

# список знаков в виде кортежей знак, максимальная дата
signs_sorted = sorted(daysandsignsdict, key=lambda x: x[1])


# Главная на гороскоп
def index(request):
    zodiacs = list(zodiac_dict)
    #f"<li><a href='{redirect_path}'>{sign.title()}<a/></li>"
    context = {
        'zodiacs' : zodiacs
    }

    return render(request, 'horoscope/index.html', context=context)


# если напишут месяц с днем
def dayandmonth(request, month, day):
    if 1 < month < 13 and day <= daysinmonthdict[month]:
        trueday = day + daysinmonthdict[month - 1]
    elif month == 1:
        trueday = day
    else:
        return HttpResponseNotFound(f"Такого месяца или дня не существует - {month}, {day}")
    for day in signs_sorted:
        if trueday <= day[1]:
            redirect_url = reverse("horoscope_name", args=[day[0]])
            return HttpResponseRedirect(redirect_url)


# Главная, типы
def typeindex(request):
    types = list(typedict)
    li_elements = ''
    for element in types:
        redirect_path = reverse('type_name', args=[element])
        li_elements += f"<li><a href='{redirect_path}'>{element.title()}</a></li>"
    response = f"""
    <ul>
    {li_elements}
    </ul>
    """
    return HttpResponse(response)


# Главная, постихийно
def elementindex(request, type):
    description = typedict.get(type)
    if description:
        li_elements = ''
        for zodiak in description:
            redirect_path = reverse('horoscope_name', args=[zodiak])
            li_elements += f"<li><a href='{redirect_path}'>{zodiak.title()}</a></li>"
        response = f"""
        <ul>
        {li_elements}
        </ul>
        """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f"Такая стихия не пойдет для знака зодиака - {type}")


# На конкретные знаки зодиака
def sign(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac)
    info = {
        'sign': sign_zodiac,
        'sign_info': description
    }
    if description:
        return render(request, 'horoscope/info_zodiak.html', info)
    else:
        return HttpResponseNotFound(f"Я не знаю таких знаков зодиака, чел - {sign_zodiac}")


# По номеру ЗЗ
def sign_by_num(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Я не знаю таких знаков зодиака, чел - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope_name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
