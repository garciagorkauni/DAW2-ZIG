from django.urls import path
from . import views

urlpatterns = [
    path('', views.ikasle_list, name='zerrenda-default'),
    path('Ikasle/new/', views.ikasle_new, name='zerrenda-ikasle-new')
]