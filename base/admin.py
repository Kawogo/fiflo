from django.contrib import admin
from .models import UserGroup,Category,File,Comment

# Register your models here.
admin.site.register(UserGroup)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Comment)