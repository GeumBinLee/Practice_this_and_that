from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserRisedNumListSerializer, GenderZipCodeSerializer, CareerPeriodSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

# 주민번호 안 1의 개수
class CountOneInRisedNumView(APIView) :
    
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary = "주민번호 안 1 세기",
        responses = {200: "성공", 404 : "찾을 수 없음", 500 : "서버 에러"},
    )
    def get(self, request) :
        users = User.objects.filter(rised_num__contains="1").order_by("emp_name")
        serializer = UserRisedNumListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# 성별 우편번호 모두 더하기
class SumZipCodeByGenderView(APIView) :
    
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_summary = "성별 우편번호 모두 더하기",
        responses = {200: "성공", 404 : "찾을 수 없음", 500 : "서버 에러"},
    )
    
    def get(self, request) :
        guys = User.objects.filter(gender = "M").order_by("emp_name")
        women = User.objects.filter(gender = "F").order_by("emp_name")
        guy_serializer = GenderZipCodeSerializer(guys, many=True)
        woman_serializer = GenderZipCodeSerializer(women, many=True)
        # return Response({'여자 우편 번호 합' : woman_serializer.data, '남자 우편 번호 합' : guy_serializer.data},
        #                 status=status.HTTP_200_OK)
        woman_sum = 0

        for w in range(len(woman_serializer.data)) :
            woman_sum += woman_serializer.data[w]['zip_cde']
        
        guy_sum = 0
        for m in range(len(guy_serializer.data)) :
            guy_sum += guy_serializer.data[m]['zip_cde']
            
        return Response({'여자 우편 번호 합' : woman_sum, '남자 우편 번호 합' : guy_sum},
                        status=status.HTTP_200_OK)


# 입사일의 전월말일 구하고 퇴사일과 차이나는 시간 구하기
# 퇴사일이 없으면 현재 일자 기준으로 구하기
class CareerPeriodView(APIView) :
    
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_summary = "재직 기간 구하기",
        responses = {200: "성공", 404 : "찾을 수 없음", 500 : "서버 에러"},
    )
    
    def get(self, request) :
        users = User.objects.all()
        serializers = CareerPeriodSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)