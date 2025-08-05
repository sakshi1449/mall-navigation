from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet, FloorViewSet, CategoryViewSet, StoreViewSet, AmenityViewSet

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'amenities', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]