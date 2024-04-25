from django.db import models

class Maqola(models.Model):
    WORLD = 'world'
    LOCAL = 'local'
    SPORT = 'sport'
    TAG = (
        ('world', WORLD),
        ('local', LOCAL),
        ('sport', SPORT)
    )
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, null =True, blank = True)
    tag = models.CharField(max_length = 255, choices=TAG)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.title}'
    
