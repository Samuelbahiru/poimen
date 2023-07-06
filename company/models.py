from django.db import models
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from unidecode import unidecode
from fontawesome_5.fields import IconField
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives


#Blog Model
class Blog_Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    
    def count_categories(self):
        return Blog.objects.filter(type__name = self.name).count()
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/image/')
    content = FroalaField()
    slug = models.SlugField(max_length=300, unique=True,blank=True)
    type = models.ManyToManyField(Blog_Categories)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def count_comment(self):
      return Blog_Comment.objects.filter(post__id = self.pk, status = True).count()
    
    def send_email(self):
     subscribers = Subscription.objects.values_list('email')
     emails = list(subscribers)
     all_email = [x for tup in emails for x in tup]

     def send_email_each(email):
       subject = self.title
       from_email = '@gmail.com'
       to_email = email
       text_content = '<!DOCTYPE html>'
       html_content = self.content
       msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
       msg.attach_alternative(html_content, "text/html")
       msg.send()
       return True
     
     send_email_fun = map(send_email_each, all_email) 
     print(list(send_email_fun)) 

    def __str__(self) -> str:
        return self.title

@receiver(pre_save, sender=Blog)
def call_my_function(sender, instance, **kwargs):
    instance.send_email()
    
class Blog_Comment(models.Model):
   name = models.CharField(max_length=200)
   email = models.EmailField()
   comment = models.TextField()
   website = models.URLField()
   post = models.ForeignKey(Blog, on_delete=models.CASCADE)
   status  = models.BooleanField(default=False)
   date = models.DateTimeField(auto_now=True)
   
   
   def __str__(self):
      return self.name
    
#Resource Model
class Resource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author_image = models.ImageField(upload_to='author/image/')
    author_description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200)
    icon = IconField()
    image = models.ImageField(upload_to='blog/image/')
    short_description = models.CharField(max_length=200)
    document_link = models.URLField(max_length=200)
    content = FroalaField()
    slug = models.SlugField(max_length=300, unique=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def count_comment(self):
      return Resource_Comment.objects.filter(post__id = self.pk, status = True).count()

    def __str__(self) -> str:
        return self.title

class Resource_Comment(models.Model):
   name = models.CharField(max_length=200)
   email = models.EmailField()
   comment = models.TextField()
   website = models.URLField(blank=True, null=True)
   post = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)
   status  = models.BooleanField(default=True)
   date = models.DateTimeField(auto_now=True)
   
   
   def __str__(self):
      return self.name
    
#Service 
class Service(models.Model):
    icon = IconField()
    image = models.ImageField(upload_to='company/service/')
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300)
    content = FroalaField()
    slug = models.SlugField(max_length=300, unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    
#Gallery 
class Gallery_Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Gallery_Categories,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='company/gallery')
    slug = models.SlugField(max_length=100, unique=True,blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


#Subscription 
class Subscription(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name