from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserRisedNumListSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

class CountOneInRisedNum(APIView) :
    
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary = "주민번호 안 1 세기",
        responses = {200: "성공", 404 : "찾을 수 없음", 500 : "서버 에러"},
    )
    def get(self, request) :
        users = User.objects.filter(rised_num__contains="1").order_by("emp_name")
        serializer = UserRisedNumListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)