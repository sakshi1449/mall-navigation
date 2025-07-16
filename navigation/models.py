from django.db import models
from stores.models import Store, Floor

class NavigationNode(models.Model):
    """
    Represents a point in the map used for pathfinding/navigation.
    Can be linked to a store or be a general coordinate node.
    """
    name = models.CharField(max_length=100, blank=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    z_coord = models.FloatField(default=0.0)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name or f"Node ({self.x_coord}, {self.y_coord}) on Floor {self.floor.level}"


class NavigationEdge(models.Model):
    """
    Represents a connection (edge) between two navigation nodes.
    """
    start_node = models.ForeignKey(NavigationNode, on_delete=models.CASCADE, related_name='edges_from')
    end_node = models.ForeignKey(NavigationNode, on_delete=models.CASCADE, related_name='edges_to')
    distance = models.FloatField(help_text="Distance between the nodes in meters")
    is_accessible = models.BooleanField(default=True, help_text="Whether this path is accessible (e.g. wheelchair accessible)")

    def __str__(self):
        return f"{self.start_node} → {self.end_node} ({self.distance}m)"


