from app1.views import *


from django.urls import path

app_name='king'

urlpatterns=[
    path('ram/',ram,name='ram'),
    path('sam/',sam,name='sam'),
]