from django.urls import path
from app1.views import app1_specific
app_name='app1'
urlpatterns=[path('app1_specific/',app1_specific,name='app1_specific'),]