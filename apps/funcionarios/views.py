from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)

from .models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa)


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', ]

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username[0] + username[1])
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos', ]


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:listar')
