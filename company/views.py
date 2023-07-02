from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
# Create your views here.
def homepage(request):
    recent_blog = models.Blog.objects.all()[:3]
    resource = models.Resource.objects.all()[:6]

    context = {
        'recent_blog' : recent_blog,
        'resources' : resource
    }
    return render(request, 'company/index.html', context)

def about(request):
    return render(request, 'company/about.html')

def contact(request):
    return render(request, 'company/contact.html')

def gallery(request):
    all_gallery = models.Gallery.objects.all()
    gallery_categories = models.Gallery_Categories.objects.all()

    context = {
        'all_gallery' : all_gallery,
        'gallery_categories': gallery_categories
    }

    return render(request, 'company/gallery.html', context)


def service(request):

    services = models.Service.objects.all()

    context = {
        'services' : services
    }

    return render(request, 'company/services.html', context)

def service_detail(request, slug):
    service_detail = models.Service.objects.filter(slug = slug).first()

    context = {
        'service' : service_detail
    }
    return render(request, 'company/service-details.html', context)

def resource(request):
    resources = models.Resource.objects.all()
    paginator = Paginator(resources, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page' : page,
    }
    return render(request, 'company/resource.html', context)

def resource_detail(request, slug):
    resource_detail = models.Resource.objects.filter(slug = slug).first()

    comment = models.Resource_Comment.objects.filter(status = True, post__id = resource_detail.id)
    
    if request.method == "POST":
      
      name = request.POST.get('name')
      email = request.POST.get('email')
      website = request.POST.get('website')
      comment = request.POST.get('comment')
      
      obj = models.Resource_Comment()
      obj.name = name
      obj.email = email
      obj.website = website
      obj.comment = comment
      obj.post = resource_detail
      obj.save()

    context = {
        'resource' : resource_detail,
        'comments' : comment
    }

    return render(request, 'company/resource-details.html', context)

def blog_detail(request, slug):

    blog_detail = models.Blog.objects.filter(slug = slug).first()
    blogs = models.Blog.objects.all()
    recent_blogs = []
    for blog in range(0,5,1):
        recent_blogs.append(blogs[blog])
    
    comment = models.Blog_Comment.objects.filter(status = True, post__id = blog_detail.id)

    if request.method == "POST":
      
      name = request.POST.get('name')
      email = request.POST.get('email')
      website = request.POST.get('website')
      comment = request.POST.get('comment')
      
      obj = models.Blog_Comment()
      obj.name = name
      obj.email = email
      obj.website = website
      obj.comment = comment
      obj.post = blog_detail
      obj.save()


    context = {
        'blog' : blog_detail,
        'categories' : models.Blog_Categories.objects.all(),
        'recent_blogs' : recent_blogs,
        'comments' : comment,
    }
    return render(request, 'company/blog-details.html', context)

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Send the email
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\n\n{message}",
            email,
            ['samuelbahiru93@gmail.com'],
            fail_silently=False,
        )

        # Return a JSON response to indicate success
        return JsonResponse({'success': True})

    # Return a JSON response to indicate an error
    return JsonResponse({'success': False})