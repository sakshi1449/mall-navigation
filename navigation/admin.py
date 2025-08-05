from django.contrib import admin
from .models import NavigationNode, NavigationEdge

@admin.register(NavigationNode)
class NavigationNodeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'floor', 'x_coord', 'y_coord', 'z_coord', 'store')
    list_filter = ('floor',)
    search_fields = ('name',)
    autocomplete_fields = ('store',)
    ordering = ('floor', 'name')


@admin.register(NavigationEdge)
class NavigationEdgeAdmin(admin.ModelAdmin):
    list_display = ('start_node', 'end_node', 'distance', 'is_accessible')
    list_filter = ('is_accessible',)
    search_fields = (
        'start_node__name',
        'end_node__name',
    )
    autocomplete_fields = ('start_node', 'end_node')
    
