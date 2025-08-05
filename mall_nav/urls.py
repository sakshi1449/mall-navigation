"""
URL configuration for mall_nav project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mall-navigation-backend/mall_nav/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views  # views.py in mall_nav

urlpatterns = [
    path('', views.login_view, name='login'),           # http://127.0.0.1:8000/
    path('index/', views.index_view, name='index'),     # After login
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),

    # App-specific API routes
    path('api/products/', include('products.urls')),
    path('api/stores/', include('stores.urls')),
    path('api/navigation/', include('navigation.urls')),  # ← your API + map view
]
