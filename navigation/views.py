from django.shortcuts import render
from rest_framework import viewsets
from .models import NavigationNode, NavigationEdge
from .serializers import NavigationNodeSerializer, NavigationEdgeSerializer

# API views
class NavigationNodeViewSet(viewsets.ModelViewSet):
    queryset = NavigationNode.objects.all()
    serializer_class = NavigationNodeSerializer

class NavigationEdgeViewSet(viewsets.ModelViewSet):
    queryset = NavigationEdge.objects.all()
    serializer_class = NavigationEdgeSerializer

# HTML view
def map_view(request):
    return render(request, 'map.html')  # or your actual template name
