from django.db import models

class MathHistory(models.Model):
    sum = models.CharField(max_length=60)
    result = models.IntegerField(default=0)    
    
