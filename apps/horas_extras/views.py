from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import HoraExtra


class HoraExtraCreateView(CreateView):
    model = HoraExtra
    fields = ['horas', 'motivo', 'funcionario', ]


class HoraExtraListView(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa)


class HoraExtraUpdateView(UpdateView):
    model = HoraExtra
    fields = ['horas', 'motivo', 'funcionario', ]


class HoraExtraDeleteView(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('horas_extras:list')
