from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Default
    path('', views.base, name='base'),

    # CRUD for Pazientea
    path('pazientea/kudeaketa/', TemplateView.as_view(template_name='osakidetza/pazientea/pazientea_kudeaketa.html'), name='pazientea-kudeaketa'),
    path('pazientea/list/', views.list_pazientea, name='list-pazientea'),
    path('pazientea/new/', views.new_pazientea, name='new-pazientea'),
    path('pazientea/delete/', views.delete_pazientea, name='delete-pazientea'),
    path('pazientea/edit/', views.edit_pazientea, name='edit-pazientea'),
    path('pazientea/edit-form/<int:pazientea_id>/', views.edit_pazientea_form, name='edit-pazientea-form'),

    # CRUD for Medikua
    path('medikua/kudeaketa/', TemplateView.as_view(template_name='osakidetza/medikua/medikua_kudeaketa.html'), name='medikua-kudeaketa'),
    path('medikua/new/', views.new_medikua, name='new-medikua'),
    path('medikua/delete/', views.delete_medikua, name='delete-medikua'),
    path('medikua/edit/', views.edit_medikua, name='edit-medikua'),
    path('medikua/edit-form/<int:medikua_id>/', views.edit_medikua_form, name='edit-medikua-form'),

    # CRUD for Zita
    path('zita/kudeaketa/', TemplateView.as_view(template_name='osakidetza/zita/zita_kudeaketa.html'), name='zita-kudeaketa'),
    path('zita/list/', views.list_zita, name='list-zita'),
    path('zita/new/', views.new_zita, name='new-zita'),
]