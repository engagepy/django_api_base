from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates, name='advocates'),
    path('advocates/<str:username>', views.advocate_details, name='details'),

]