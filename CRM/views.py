from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages


def contacts(request):
    page_name = 'contacts'
    form = MessageForm()
    if request.method == 'POST':
        message = MessageForm(request.POST)
        if message.is_valid():
            new_message = message.save(commit=False)
            new_message.user = request.user.id
            new_message.save()
            messages.add_message(request, messages.INFO, 'Сообщение отправлено')
    context = {
        'form':form,
        'page_name':page_name
    }
    return render(request, 'contacts.html', context)
