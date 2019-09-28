from django.urls import path
from . import views

urlpatterns = [
    path('institution', views.InstitutionListCreate.as_view()),
    path('equipment', views.EquipmentListCreate.as_view()),
]