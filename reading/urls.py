from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name= 'index'),
    ]




# urlpatterns = [
#     path('', views.index, name= 'index'),
#     path('obrero/', views.obrero, name= 'index'),
#     path('cdso/', views.obrero, name= 'index'), #seudonimo obrero

# ]