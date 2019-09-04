import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .forms import HoraExtraForm
from .models import HoraExtra


class HoraExtraCreateView(CreateView):
    model = HoraExtra
    form_class = HoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraListView(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa)


class HoraExtraUpdateView(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDeleteView(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('horas_extras:list')


class UtilizarHoraExtraView(View):
    def post(self, *args, **kwargs):
        hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        hora_extra.utilizada = True
        hora_extra.save()

        funcionario = self.request.user.funcionario
        response = json.dumps({'mensagem': 'Requisição executada.', 'horas': float(funcionario.total_horas)})

        return HttpResponse(response, content_type='application/json')
