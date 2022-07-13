from django.http import HttpResponse


def index(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('<h2>Здесь будет карта</h2>')
