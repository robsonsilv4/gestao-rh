from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class HoraExtra(models.Model):
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('horas_extras:atualizar', args=self.id)

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extras'
