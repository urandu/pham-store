from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/institution/', views.InstitutionListCreate.as_view()),
    path('api/v1/equipment/', views.EquipmentListCreate.as_view()),
    path('api/v1/equipment/<int:pk>', views.EquipmentRetrieveUpdate.as_view()),
    path('health/', views.HealthCheck.as_view()),
]