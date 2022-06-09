from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='about'),
    path('contact/', contact, name='about'),
    path('main/', main, name='about'),
    path('single-blog/', single_blog, name='about'),
    path('track/', track, name='about'),
]