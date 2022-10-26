from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates, name='advocates'),
    # path('advocates/<str:username>', views.advocate_details, name='advocate_details'),
    path('advocates/<str:username>', views.AdvocateDetails.as_view(), name='advocate_details'),
    path('company/', views.companies_list, name='comapny_details'),
]