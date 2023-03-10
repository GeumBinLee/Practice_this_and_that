from django.urls import path
from users import views

urlpatterns = [
    path("", views.CountOneInRisedNum.as_view(), name="count_one_in_rised_num"),
]