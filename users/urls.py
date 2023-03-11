from django.urls import path
from users import views

urlpatterns = [
    path("rised_num/", views.CountOneInRisedNumView.as_view(), name="count_one_in_rised_num"),
    path("zip_code/", views.SumZipCodeByGenderView.as_view(), name="sum_of_zip_code_group_by_gender"),
    path("career_period/", views.CareerPeriodView.as_view(), name="career_period"),
    path("rised_num_with_star/", views.UserRisedNumWithStarView.as_view(), name="rised_num_with_star"),
]