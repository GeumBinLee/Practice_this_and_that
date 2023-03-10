from rest_framework import serializers
from .models import User



class UserRisedNumListSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = User
        fields= ("emp_name","rised_num",)
        
    rised_num = serializers.SerializerMethodField()
    
    def get_rised_num(self, obj) :
        return obj.rised_num.count("1")