from django.urls import path
from . import views

urlpatterns=[

    path('verification', views.verification, name='verification'),
    path('profile', views.profile, name='profile'),
    path('verify_form2', views.verify_form2, name='verify_form2'),
        
]