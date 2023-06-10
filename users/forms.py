from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django import forms


class UserRegistrationForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    # email = forms.EmailField(widget = forms.EmailInput(attrs={'class' : 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','role']
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'js-states form-control'
        

class UserUpdateForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(),required=False)

    class Meta:
        model = User
        fields = ['username','email','role'] 
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'js-states form-control'

