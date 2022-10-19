from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from ShopApp.utils import menu
from django.conf import settings


def contact_form(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['from_email']
            recipient_list = 'bondarenkowrite@gmail.com'
            email_from = settings.EMAIL_HOST_USER
            try:
                send_mail(f'Обратная связь от {name}', f'Получено от пользователя: {name}\n'
                                                       f'Почтовый ящик пользователя: {user_email}\n'
                                                       f'{message}\n'
                                                       f'Ответить по почте {user_email}. Дать обратную связь!',
                          email_from, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Ошибка связи.')
            return redirect('feedback:success')
    else:
        return HttpResponse('Неверный запрос.')
    context = {
        'title': 'Обратная связь',
        'menu': menu,
        'form': form,
    }
    return render(request, 'feedback/feedback_form.html', context=context)


def success(request):
    context = {
        'title': 'Успех',
        'menu': menu,
    }
    return render(request, 'feedback/success_feedback.html', context=context)
