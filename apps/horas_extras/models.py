from django.db import models

from apps.funcionarios.models import Funcionario


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extras'
