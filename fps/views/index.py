from django.http import HttpResponse

def index(request):
    return HttpResponse("FPS后端揭界面！！！")
