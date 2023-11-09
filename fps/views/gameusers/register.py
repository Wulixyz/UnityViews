from django.http import HttpResponse,JsonResponse
from fps.models import GameUsers

def register(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')

    if GameUsers.objects.filter(username=username).exists():
        return JsonResponse({
            'error_message': "username has existed"
        })

    GameUsers.objects.create(username=username,password=password)

    return JsonResponse({
        'error_message': "success",
        'username': username,
        'password': password,
    })
