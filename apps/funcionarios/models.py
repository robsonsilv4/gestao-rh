from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_horas(self):
        return self.horaextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum'] or 0

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('funcionarios:listar')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
