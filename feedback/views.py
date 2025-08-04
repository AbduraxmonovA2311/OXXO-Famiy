from django.shortcuts import render, redirect
from .forms import FeedbackForm
import requests
import requests
from django.shortcuts import render
from .forms import FeedbackForm

TELEGRAM_BOT_TOKEN = '7851533433:AAHEM80NgRk_hdqYRllraCpw5iA5l8mp8x0'
TELEGRAM_CHAT_ID = '2042989665'

def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=data)

def home(request):
    submitted = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rating = form.cleaned_data['rating']
            message = form.cleaned_data['message']

            # Telegramga yuboriladigan matn
            telegram_message = (
               f"Yangi fikr keldi:\n"
            f"👤 Ismi: {name}\n"
            f"⭐ Bahosi: {rating}\n"
            f"💬 Xabar: {message}"
            )
            send_to_telegram(telegram_message)
            form.save()
            submitted = True
    else:
        form = FeedbackForm()

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
