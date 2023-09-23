from django.urls import path #path function
from . import views 

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    # path('home/', views.landing),
    # path('menu/', views.menu,name = 'menu')
]
