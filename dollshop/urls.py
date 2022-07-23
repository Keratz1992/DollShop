
from django.urls import path



from dollshop.views import homepage

app_name = 'dollshop'

urlpatterns = [
    path('', homepage, name='homepage')
]
