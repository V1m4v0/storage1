from django.shortcuts import render
from .forms import User_Register
from .models import Buyer, Game
from django.http import HttpResponse

def platform(request):
    return render(request, 'first_task/platform.html')

def shop(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'first_task/shop.html', context)

def basket(request):
    return render(request, 'first_task/basket.html')

def menu(request):
    return render(request, 'first_task/menu.html')

def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        form = User_Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and username not in users and int(age) >= 18:
                Buyer.objects.create(name=username, balance=1500.0, age=age)
                return render(request, 'first_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': User_Register()})

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'

    else:
        form = User_Register()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)



def sign_up_by_html(request):
    return sign_up_by_django(request)