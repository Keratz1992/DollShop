
from django.urls import path

from dollshop.views import homepage

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name='homepage')
]
