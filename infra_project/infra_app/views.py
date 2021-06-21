from django.http import HttpResponse


def index(request):
    return HttpResponse('OK! У меня получилось!')


def second_page(request):
    return HttpResponse('OK! А это вторая страница')
