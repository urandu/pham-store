from rest_framework import serializers

from pharm_store_api.models import Institution, Equipment


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'industry', 'contact_person')

class EquipmentSerializer(serializers.ModelSerializer):
    institution = serializers.RelatedField(source='institution.name', read_only=True)
    class Meta:
        model = Equipment
        fields = ('name', 'quantity', 'created_by', 'institution')
