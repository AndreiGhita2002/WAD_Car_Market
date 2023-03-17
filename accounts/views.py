from django.shortcuts import render
from accounts.forms import CreateUserForm, UpdateUserProfileForm, UpdateUserForm, UserProfileForm
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            UserProfile.objects.create(
				user=user,
				)
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = CreateUserForm()

    return render(request, 'accounts/register.html', context = {'user_form': user_form, 'registered': registered})

@login_required   
def profile(request):
    user_profile = request.user.userprofile
    user = request.user
    user_form = UpdateUserForm(instance=user)
    profile_form = UpdateUserProfileForm(instance=user_profile)
    picture_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        profile_form = UpdateUserProfileForm(request.POST, request.FILES,instance=user_profile)
        picture_form = UserProfileForm(request.POST, request.FILES,instance=user_profile)
        user_form = UpdateUserForm(request.POST,instance=user)

        if profile_form.is_valid() and user_form.is_valid() and picture_form.is_valid():
            profile_form.save()
            picture_form.save()
            user_form.save()
    
    context = {'profile_form': profile_form, 'user_form': user_form, 'picture_form':picture_form}
    return render(request, 'accounts/profile.html', context)

