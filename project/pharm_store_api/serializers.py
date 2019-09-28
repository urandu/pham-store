from rest_framework import serializers

from pharm_store_api.models import Institution, Equipment


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'industry', 'contact_person')

class EquipmentSerializer(serializers.ModelSerializer):
    inst = serializers.HyperlinkedRelatedField(view_name='institution_name')
    class Meta:
        model = Equipment
        # fields = ('name', 'quantity', 'created_by', 'institution')
        fields = '__all__'
