from django.urls import path
from .views import func_template

urlpatterns = [
    path('', func_template, name='home'),
]
