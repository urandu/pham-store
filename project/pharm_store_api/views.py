from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from pharm_store_api.models import Institution, Equipment
from pharm_store_api.serializers import EquipmentSerializer, InstitutionSerializer
from rest_framework import generics

class InstitutionListCreate(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class EquipmentListCreate(generics.ListCreateAPIView):
    Equipment.objects.all().delete()
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['institution', 'created_at']

class EquipmentRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer