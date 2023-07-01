from django.db import models
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from unidecode import unidecode

class Blog_Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    
    def count_categories(self):
        return Blog.objects.filter(__type = self.name).count()
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/image/')
    content = FroalaField()
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    type = models.ManyToManyField(Blog_Categories)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    

