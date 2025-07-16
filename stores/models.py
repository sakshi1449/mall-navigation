from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)

    def _str_(self):
        return self.name

class Floor(models.Model):
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Level {self.level})"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    z_coord = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.store.name}"

