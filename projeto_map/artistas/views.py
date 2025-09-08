from django.shortcuts import redirect, render
from django.views import View
from .models import Perfil


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        # Lógica de autenticação aqui
        email = request.POST.get('username')
        senha = request.POST.get('password')

        if not email or not senha:
            return render(request, 'login.html', {'error': 'Preencha todos os campos.'})

        if Perfil.objects.filter(email=email).exists():
            return render(request, 'login.html', {'error': 'email já cadastrado.'})
        
        Perfil.objects.create(email=email, senha=senha)


        return redirect('home')


class Home(View):
    def get(self,request):
        return render(request, 'home.html')

