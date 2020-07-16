from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('relative/',views.re_url,name='relative'),
    path('other/',views.other,name='other'),
]
