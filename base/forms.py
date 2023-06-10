from django.forms import ModelForm
from django import forms
from .models import UserGroup,Category,File,Comment


class UserGroupForm(forms.ModelForm):
    """Form definition for UserGroup."""

    class Meta:
        """Meta definition for UserGroupform."""

        model = UserGroup
        fields = ('name','description','members')
    
    def __init__(self, *args, **kwargs):
        super(UserGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['members'].widget.attrs['class'] = 'form-control'
        
        
        
class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = ['category_name']
    
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs['class'] = 'form-control'
   
   
   
        
class UploadFileForm(forms.ModelForm):
    """Form definition for UploadFile."""

    class Meta:
        """Meta definition for UploadFileform."""

        model = File
        fields = ['file','category','description','group']
    
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['group'].widget.attrs['class'] = 'form-control'
        
class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ""
        self.fields['comment'].widget.attrs['class'] = 'widget-chat-compose-input form-control flex-fill'
        self.fields['comment'].widget.attrs['placeholder'] = 'Type comment here...'
        


