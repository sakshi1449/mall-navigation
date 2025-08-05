from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NavigationNodeViewSet, NavigationEdgeViewSet

router = DefaultRouter()
router.register(r'nodes', NavigationNodeViewSet)
router.register(r'edges', NavigationEdgeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),            # API: /api/nodes/, /api/edges/
    path('', views.map_view, name='map'),          # HTML map page: /
    path('map/', views.map_view, name='mall-map'), # Optional: /map/
]

