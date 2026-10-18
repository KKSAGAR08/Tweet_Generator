from django.urls import path
from .views import home_page_view,form_page_view,get_django_ram_usage

urlpatterns = [
    path('',home_page_view,name='home_page'),
    path('form/',form_page_view,name='form_page'),
    path('ram/',get_django_ram_usage,name='ram'),
]
