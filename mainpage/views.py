from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")

def simple_view(request):
    context = {"string": "Путешествия — это особый способ познания мира и самого себя. Они открывают перед человеком новые горизонты, позволяют увидеть жизнь в других красках и почувствовать ритм незнакомых городов и стран. Каждая дорога — это история, наполненная встречами, открытиями и впечатлениями, которые остаются в памяти на долгие годы."}
    return render(request, "infobar.html", context)