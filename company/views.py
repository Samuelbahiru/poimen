from django.shortcuts import render
from . import models

# Create your views here.
def homepage(request):
    blogs = models.Blog.objects.all()
    recent_blog = []
    for blog in range(0,3,1):
        recent_blog.append(blogs[blog])
    
    print(recent_blog)


    context = {
        'recent_blog' : recent_blog
    }
    return render(request, 'company/index.html', context)

def about(request):
    return render(request, 'company/about.html')

def contact(request):
    return render(request, 'company/contact.html')

def project(request):
    return render(request, 'company/projects.html')

def project_detail(request):
    return render(request, 'company/project-details.html')

def service(request):
    return render(request, 'company/services.html')

def service_detail(request):
    return render(request, 'company/service-details.html')

def blog(request):
    return render(request, 'company/blog.html')

def blog_detail(request, slug):
    blog = models.Blog.objects.filter(slug = slug).first()
    context = {
        'blog' : blog
    }
    return render(request, 'company/blog-details.html', context)