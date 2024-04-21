from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        #verifica se senha e confirmar senha são iguais
        if senha != confirmar_senha:
            print('Erro 2')
            return redirect('/usuarios/cadastro')
        #verifica se a senha tem mais de 6 dígitos
        if len(senha) < 6:
            print('erro 3')
            return redirect('/usuarios/cadastro')

        users = User.objects.filter(username=username)
        print(users.exists())
        
        if users.exists():
            print('Erro1')
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        return HttpResponse(f'Usuário Criado com sucesso')