from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inicio(request):
    data = {
        'usuario': request.user
    }
    return render(request, 'base/inicio.html', data)
