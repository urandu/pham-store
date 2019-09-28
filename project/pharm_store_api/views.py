from django.shortcuts import render
from project.pharm_store_api.models import Institution, Equipment
from project.pharm_store_api.serializers import EquipmentSerializer, InstitutionSerializer
from rest_framework import generics

class InstitutionListCreate(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

