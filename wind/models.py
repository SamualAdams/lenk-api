from django.db import models

class WindData(models.Model):
    name = models.CharField(max_length=100)
    speed = models.FloatField()
    direction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.speed} mph {self.direction}"
