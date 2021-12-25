#import forms from django
#import user models and custom user model that we created
from django import forms
from django.contrib.auth.models import User
from app_users.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta():
        model=User
        fields=('username','first_name','last_name','password1','password2')
        labels={
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio=forms.CharField(required=False)
    teacher='teacher'
    student='student'
    parent='parent'
    user_types=[
        (student,'student'),
        (parent,'parent'),
    ]
    user_type=forms.ChoiceField(required=True,choices=user_types)
    class Meta():
        model=user_profile
        fields=('bio','profile_pic','user_type')
