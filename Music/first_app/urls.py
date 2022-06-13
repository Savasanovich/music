from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('main/', main, name='main'),
    path('single-blog/', single_blog, name='single-blog'),
    path('tracks/', track, name='tracks'),
]