from django.db import models


class Documento(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extras'
