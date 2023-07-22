from django.shortcuts import render
from . import models
from . import forms
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.
def homepage(request):
    recent_blog = models.Blog.objects.all()[:3]
    resource = models.Resource.objects.all()[:6]

    if request.method == 'POST':
        form = forms.SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.SubscriptionForm()
    else:
        form = forms.SubscriptionForm()

    
    context = {
        'recent_blog' : recent_blog,
        'resources' : resource
    }
    return render(request, 'company/index.html', context)

def about(request):
    return render(request, 'company/about.html')

def donate(request):
    return render(request, 'company/donate.html')
def contact(request):
     return render(request, 'company/contact.html')

def news(request):

    blogs = models.Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page' : page,
        'blogs' : blogs,
        'categories' : models.Blog_Categories.objects.all(),
    }
   
    
    return render(request, 'company/news.html', context)


def service(request):

    services = models.Service.objects.all()

    context = {
        'services' : services,
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
    resource_detail = models.Resource.objects.get(slug = slug)
    comment = models.Resource_Comment.objects.filter(post__pk = resource_detail.pk, status = True)
    
    form = forms.ResourceComment()
    context = {
        'resource' : resource_detail,
        'comment' : comment,
        'form' : form
    }
    if request.method == 'POST':
        form = forms.ResourceComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = resource_detail
            comment.save()
            return render(request, 'company/resource-details.html', context)

    return render(request, 'company/resource-details.html', context)



def blog_detail(request, slug):

    blog_detail = models.Blog.objects.filter(slug = slug).first()
    recent_blogs = models.Blog.objects.all()[:5]
    comment = models.Blog_Comment.objects.filter(status = True, post__id = blog_detail.id)

    form = forms.BlogComment()

    context = {
        'blog' : blog_detail,
        'categories' : models.Blog_Categories.objects.all(),
        'recent_blogs' : recent_blogs,
        'comments' : comment,
        'form' : form
    }
    if request.method == 'POST':
        form = forms.BlogComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_detail
            comment.save()
            form = forms.BlogComment()     
            return render(request, 'company/blog-details.html', context)
    
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
            ['poimenkb@gmail.com'],
            fail_silently=True,
        )

        # Return a JSON response to indicate success
        return JsonResponse({'success': True})

    # Return a JSON response to indicate an error
    return JsonResponse({'success': True})