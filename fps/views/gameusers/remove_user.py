from django.http import HttpResponse,JsonResponse
from fps.models import GameUsers

def remove_user(request):
    username = request.GET.get('username')

    if GameUsers.objects.filter(username=username).exists():
        GameUsers.objects.filter(username=username).delete()
        return JsonResponse({
            'error_message': "success",
            'username': username,
        })

    return JsonResponse({
        'error_message': "fail to remove",
    })
