from django.shortcuts import render
from accounts.forms import CreateUserForm
from accounts.models import UserProfile

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = CreateUserForm()

    return render(request, 'accounts/register.html', context = {'user_form': user_form, 'registered': registered})
    
def profile(request):
    return render(request, 'core/home.html', context = {})