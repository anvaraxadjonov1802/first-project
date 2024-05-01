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
    image = models.ImageField()
    tag = models.CharField(max_length = 255, choices=TAG)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add = True)

    @property
    def imageURL(self):
        return self.image.url
    
    def __str__(self) -> str:
        return f'{self.id} --- {self.title}'
    
