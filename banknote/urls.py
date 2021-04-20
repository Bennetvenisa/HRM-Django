from django.urls import path
from . import views

urlpatterns=[

        path('banknote', views.banknote, name='banknote'),
]


