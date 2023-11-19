from django.urls import path
from sales.views import listorders,  listorders1

urlpatterns = [
  path('order/', listorders),
  path('order1/', listorders1)
]