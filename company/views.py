from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'company/index.html')

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

def blog_detail(request):
    return render(request, 'company/blog-details.html')