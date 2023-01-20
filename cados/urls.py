from django.urls import path
from . import views

urlpatterns = [
        path('', views.endpoints),
        path('advocates/', views.advocate_list, name="adcocates"),
        # path('advocates/<str:username>/', views.advocate_detail),
        
        # CLASS BASED VIEW URL
        path('advocates/<str:username>/', views.AdvocateDetail.as_view()),
        path('companies/', views.company_list),
]