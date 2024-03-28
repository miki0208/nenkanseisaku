from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage


def index(request):
    return render(request, 'finish.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        emailMessage = EmailMessage(
            to=['vahohe4664@soebing.com'],
            subject='お問い合わせがありました：{0}'.format(subject),
            body='名前: {0}\nメールアドレス: {1}\n本文: {2}'.format(name, email, message),
        )
        emailMessage.send()
        return HttpResponseRedirect('send/')
    else:
        return render(request, 'contact.html')

