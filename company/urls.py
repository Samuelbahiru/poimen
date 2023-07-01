from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project, name='project'),
    path('project/',views.project_detail, name='project_detail'),
    path('services/', views.service, name='service'),
    path('service/', views.service_detail, name='service_detail'),
    path('blogs/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail')
]