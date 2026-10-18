from django.urls import path
from .views import home_page_view,form_page_view

urlpatterns = [
    path('',home_page_view,name='home_page'),
    path('form/',form_page_view,name='form_page'),
]
