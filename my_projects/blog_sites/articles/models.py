from django.db import models

class Maqola(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, null =True, blank = True)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.title}'
    
