from django.forms import ModelForm

from apps.funcionarios.models import Funcionario
from .models import HoraExtra


class HoraExtraForm(ModelForm):
    class Meta:
        model = HoraExtra
        fields = ['horas', 'motivo', 'funcionario', ]

    def __init__(self, user, *args, **kwargs):
        super(HoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)
