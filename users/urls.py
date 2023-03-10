from django.urls import path
from users import views

urlpatterns = [
    path("rised_num/", views.CountOneInRisedNum.as_view(), name="count_one_in_rised_num"),
    path("zip_code/", views.SumZipCodeByGender.as_view(), name="sum_of_zip_code_group_by_gender"),
]