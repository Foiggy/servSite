from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Привет! С вами говорит Джанго-релизнутый</h1>")

def secretURL(request):
    return HttpResponse("<h1>Опа! Как ты меня нашел?</h1>")

# Create your views here.
