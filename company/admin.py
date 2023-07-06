from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Blog)
admin.site.register(models.Blog_Categories)
admin.site.register(models.Blog_Comment)
admin.site.register(models.Resource)
admin.site.register(models.Service)
admin.site.register(models.Gallery)
admin.site.register(models.Gallery_Categories)
admin.site.register(models.Resource_Comment)
admin.site.register(models.Subscription)