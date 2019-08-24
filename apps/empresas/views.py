from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView

from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome', ]

    def form_valid(self, form):
        empresa = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = empresa
        funcionario.save()
        return HttpResponse('Ok!')


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nome', ]
