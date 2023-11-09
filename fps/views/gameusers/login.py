from django.http import HttpResponse,JsonResponse
from fps.models import GameUsers

def login(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')

    if not GameUsers.objects.filter(username=username).exists():
        return JsonResponse({
            'error_message': "not exist user",
        })

    user = GameUsers.objects.get(username=username)

    if password == user.password:
        return JsonResponse({
            'error_message': "success",
        })
    return JsonResponse({
        'error_message': "username of password error",
    })
