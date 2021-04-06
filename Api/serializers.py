from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'nom_complet', 'password']
        