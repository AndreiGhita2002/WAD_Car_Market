from django import forms

class MessageForm(forms.Form):
    recipient_username = forms.CharField(max_length=128)
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    message = forms.CharField(max_length=128, widget=forms.Textarea)


