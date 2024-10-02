from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.ikasle_list, name='zerrenda-default'),

    path('ikasle-kudeaketa/', TemplateView.as_view(template_name='FirstApp/kudeaketa/ikasle/ikasle_kudeaketa.html'), name='ikasle-kudeaketa'),
    path('nota-kudeaketa/', TemplateView.as_view(template_name='FirstApp/kudeaketa/nota/nota_kudeaketa.html'), name='nota-kudeaketa'),
    path('ikasgai-kudeaketa/', TemplateView.as_view(template_name='FirstApp/kudeaketa/ikasgai/ikasgai_kudeaketa.html'), name='ikasgai-kudeaketa'),

    path('new-ikasle/', views.ikasle_new, name='zerrenda-ikasle-new'),

    path('nota-list/', views.nota_list, name='nota-list'),
    path('new-nota/', views.nota_new, name='new-nota'),

    path('ikasgai-list/', views.ikasgai_list, name='ikasgai-list'),
    path('new-ikasgai/', views.ikasgai_new, name='new-ikasgai'),
]