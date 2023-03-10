from rest_framework import serializers
from .models import User



class UserRisedNumListSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = User
        fields= ("emp_name","rised_num",)
        
    rised_num = serializers.SerializerMethodField()
    
    def get_rised_num(self, obj) :
        return obj.rised_num.count("1")
    
    
    
class GenderZipCodeSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = User
        fields = ("emp_name", "zip_cde",)
    
    zip_cde = serializers.SerializerMethodField()
    
    def get_zip_cde(self, obj) :
        str_code = "".join(obj.zip_cde.split('-'))
        return int(str_code)