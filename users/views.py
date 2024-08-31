from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import User

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is not None:
                login(request, user)
                return redirect('1')
        contex = {
            'form': form,
            'error': form.errors,
        }
        return render(request, self.template_name, contex)
