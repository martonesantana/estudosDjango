from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.



def index(request):
    return render (request, 'index.html')

def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']

            print('Mensagem enviada')
            print(f'Nome: {name}')
            print(f'E-mail: {email}')
            print(f'Assunto: {title}')
            print(f'Mensagem: {message}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render (request, 'contact.html', context)

def company(request):
    return render (request, 'company.html')