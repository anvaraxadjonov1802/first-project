from django.urls import path
from .views import *

urlpatterns = [
    path('home/', maqola, name='maqola'), 
    path('world/', world_news, name='world'),
    path('local/', local_news, name='local'),
    path('sport/', sport_news, name='sport')

]