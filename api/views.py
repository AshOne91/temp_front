from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User

@api_view(['GET'])
def hello(request):
    return JsonResponse({"message": "Hello from Django!"})

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not (username and email and password):
        return Response({"success": False, "msg": "필수 항목 누락"}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"success": False, "msg": "이미 존재하는 아이디"}, status=400)
    User.objects.create(username=username, email=email, password=password)
    return Response({"success": True, "msg": "가입 성공!"})

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username, password=password)
        return Response({"success": True, "msg": "로그인 성공!"})
    except User.DoesNotExist:
        return Response({"success": False, "msg": "아이디 또는 비밀번호 오류"}, status=400)