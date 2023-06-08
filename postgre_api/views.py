from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json

from .models import User

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        surname = data['surname']
        sexe = data['sexe']
        email = data['email']
        password = make_password(data['password'])
        age = data['age']
        weight = data['weight']
        height = data['height']
        profession = data['profession']
        user = User(name=name, surname=surname, sexe=sexe, email=email, password=password, age=age, weight=weight, height=height, profession=profession)
        user.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def authenticate_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=401)
        except User.DoesNotExist:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)

