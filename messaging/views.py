from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import MessageForm
from django.contrib.auth.decorators import login_required


#This is to message sellers, this uses the django send mail function. It redirects users if succesful to a succesful page.
@login_required
def message_seller(request):
    user_exist = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient_username = form.cleaned_data['recipient_username']
            message = form.cleaned_data['message']

            # Retrieve the seller's email address
            try:
                recipient_user = User.objects.get(username=recipient_username)
                recipient_email = recipient_user.email
                user_exist = True
            except User.DoesNotExist:
                recipient_email = None

            # Send the email
            if recipient_email:
                subject = f'{name} is interested in your car'
                message = f'{message} ; Please contact 'f'{email}'
                sender_email = email
                send_mail(subject, message, sender_email, [recipient_email], fail_silently=False,
                          )
            return render(request, 'messaging/success.html', {'user_exist': user_exist})
    else:
        form = MessageForm()

    return render(request, 'message_seller.html', {'form': form, 'user_exist': user_exist})
