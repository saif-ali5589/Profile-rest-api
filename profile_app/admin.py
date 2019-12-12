from django.contrib import admin

# Register your models here.
#u can add model in your admin interface

from profile_app import models

admin.site.register(models.UserProfile)
