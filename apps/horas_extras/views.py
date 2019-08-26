from django.urls import reverse_lazy
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
        kwargs = super(HoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDeleteView(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('horas_extras:list')
