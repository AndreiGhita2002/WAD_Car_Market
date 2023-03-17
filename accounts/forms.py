from django import forms
from django.forms import ModelForm
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username',}))
    email = forms.EmailField(max_length=75, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your email',}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your first name',}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your last name',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'retype your password',}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', }))

class UpdateUserProfileForm(ModelForm):
    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your address', 'class':"form-control mb-1"}))
    class Meta:
        model = UserProfile
        fields = ('address',)

class UpdateUserForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username','class':"form-control mb-1"}))
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'placeholder': 'Your email', 'class':"form-control mb-1"}))
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your first name', 'class':"form-control mb-1"}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your last name', 'class':"form-control mb-1"}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserProfileForm(ModelForm):
    profilePicture = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Image', 'class':'account-settings-fileinput'}))
    class Meta:
        model = UserProfile
        fields = ('profilePicture',)



