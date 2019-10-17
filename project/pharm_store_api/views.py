from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from pharm_store_api.models import Institution, Equipment
from pharm_store_api.serializers import EquipmentSerializer, InstitutionSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class InstitutionListCreate(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['institution', 'created_at']

class EquipmentRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class HealthCheck(APIView):
    def post(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)