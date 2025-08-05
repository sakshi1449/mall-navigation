
from rest_framework import serializers
from .models import NavigationNode, NavigationEdge

class NavigationNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationNode
        fields = '__all__'

class NavigationEdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationEdge
        fields = '__all__'
