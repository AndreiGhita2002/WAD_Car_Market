from django import forms

class MessageForm(forms.Form):
    recipient = forms.CharField(max_length=128, help_text="recipient")
    first_name = forms.CharField(max_length=128, help_text="first name")
    last_name = forms.CharField(max_length=128, help_text="surname")
    email = forms.EmailField(max_length=128, help_text="email")
    body = forms.CharField(widget=forms.Textarea, help_text="your message")


