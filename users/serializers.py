from rest_framework import serializers
from .models import User
from django.utils import timezone



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
    


class CareerPeriodSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = User
        fields = ("emp_name", "ent_date", "retire_date",)
        
        retire_date = serializers.SerializerMethodField()
        
        def get_retire_date(self, obj) :
            last_month_last_day = obj.ent_date - timezone.timedelta(months=1)
            if not obj.retire_date :
                diff = timezone.now() - last_month_last_day
            else :
                diff = obj.retire_date - last_month_last_day
            return type(obj.retire_date)