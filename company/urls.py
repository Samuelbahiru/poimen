from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.service, name='service'),
    path('service/', views.service_detail, name='service_detail'),
    path('resources/', views.resource, name='resource'),
    path('resource/<slug:slug>/', views.resource_detail, name='resource_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail')
]
