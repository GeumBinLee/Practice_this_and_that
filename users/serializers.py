from rest_framework import serializers
from .models import User
from django.utils import timezone


class UserRisedNumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "emp_name",
            "rised_num",
        )

    rised_num = serializers.SerializerMethodField()

    def get_rised_num(self, obj):
        return obj.rised_num.count("1")


class UserRisedNumWithStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "emp_name",
            "rised_num",
        )

    rised_num = serializers.SerializerMethodField()

    def get_rised_num(self, obj):
        rn = ""
        if obj.rised_num:
            rn = (
                obj.rised_num.split("-")[0]
                + "-"
                + "*" * len(obj.rised_num.split("-")[1])
            )
        return rn


class GenderZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "emp_name",
            "zip_cde",
        )

    zip_cde = serializers.SerializerMethodField()

    def get_zip_cde(self, obj):
        str_code = "".join(obj.zip_cde.split("-"))
        return int(str_code)


class CareerPeriodSerializer(serializers.ModelSerializer):
    ent = serializers.DateField(
        format="%Y-%m-%d",
        input_formats="%Y-%m-%d",
        source="ent_date",
        read_only=True,
        default=timezone.now,
    )
    retire = serializers.DateField(
        format="%Y-%m-%d",
        input_formats="%Y-%m-%d",
        source="retire_date",
        read_only=True,
        default=timezone.now,
    )

    class Meta:
        model = User
        fields = (
            "emp_name",
            "ent",
            "retire",
        )
