from rest_framework import serializers
from apps.services import models
from apps.auth.seriazliers import RegisterUserSerializer

class ServiceOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceOrderItem
        fields = ['id','service', 'item_type', 'length', 'title', 'description', 'person']
        extra_kwargs = {
            'service': {'required': True},
            'title': {'required': True}
        }

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceType
        fields = ['id','name']

class TeamSerializer(serializers.ModelSerializer):
    members = RegisterUserSerializer(read_only=True, many=True)
    class Meta:
        model = models.Team
        fields = ['id', 'service', 'name', 'members']

class ServiceSerializer(serializers.ModelSerializer):
    service_order_items = ServiceOrderItemSerializer(read_only=True, many=True)
    service_teams = serializers.PrimaryKeyRelatedField(queryset=models.Team.objects.all(), many=True)
    service_type_name = serializers.CharField(source="service_type.name", required=False)
    class Meta:
        model = models.Service
        fields = ['id', 'service_type', 'service_type_name', 'date', 'title', 'time', 'service_order_items','service_teams']
        extra_kwargs = {
            'service_type': {'required': True},
            'date': {'required': True},
            'time': {'required': True},
            } 
    