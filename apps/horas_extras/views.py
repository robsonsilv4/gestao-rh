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
        kwargs = super(HoraExtraUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraPaginaUpdateView(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm
    # success_url = reverse_lazy('horas_extras:atualizar')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraPaginaUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('horas_extras:atualizar-pagina', args=[self.object.id])


class HoraExtraDeleteView(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('horas_extras:list')
