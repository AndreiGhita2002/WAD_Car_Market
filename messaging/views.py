from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import MessageForm


def message_seller(request):
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
            except User.DoesNotExist:
                recipient_email = None

            # Send the email
            if recipient_email:
                subject = f'{name} is interested in your car'
                message = f'{message}'
                sender_email = email
                send_mail(subject, message, sender_email, [recipient_email], fail_silently=False,
                          reply_to=[sender_email])

            return render(request, 'success.html')
    else:
        form = MessageForm()

    return render(request, 'message_seller.html', {'form': form})
