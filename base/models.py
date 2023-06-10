from django.db import models
from django.contrib.auth.models import User
# from .models import UserGroup
import os

# Create your models here.

# user group model
class UserGroup(models.Model):
    name = models.CharField(max_length=200,null=False)
    description = models.TextField(null=True,blank=True)
    members = models.ManyToManyField(User, related_name='members')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at','created_at']
    
    def __str__(self) -> str:
        return self.name


# category model
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at','created_at']
    
    def __str__(self) -> str:
        return self.category_name



# file comments model
class Comment(models.Model):
    """Model definition for comment."""

    # TODO: Define fields here
    comment = models.CharField(null=True, blank=True, max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at','-created_at']



# file model
class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(null=True,blank=True)
    status = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    approved_status = models.IntegerField(default=0, null=True, blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete = models.CASCADE,null=True, blank=True)
    group = models.ManyToManyField(UserGroup, related_name='groups')
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    comments = models.ManyToManyField(Comment, null=True, blank=True, related_name='comments')
    
    
    class Meta:
        ordering = ['-updated_at','-created_at']
    
    # def __str__(self) -> str:
    #     return self.file
    
    def filename(self):
        return os.path.basename(self.file.name)
    


