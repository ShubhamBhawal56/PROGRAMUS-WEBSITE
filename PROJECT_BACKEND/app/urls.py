from django.urls import path
from app import views
urlpatterns=[
path('',views.register,name="register"),
path('/thankyou',views.index,name="index")
]
