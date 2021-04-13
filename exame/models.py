from django.db import models
from django.contrib.auth.models import User


class Exame(models.Model):

    def __str__(self):
        return str(self.pk)

    febre = models.BooleanField(default=False)
    tosse = models.BooleanField(default=False)
    cansaco = models.BooleanField(default=False)
    desconforto = models.BooleanField(default=False)
    dor_garganta = models.BooleanField(default=False)
    diarreia = models.BooleanField(default=False)
    conjuntivite = models.BooleanField(default=False)
    dor_cabeca = models.BooleanField(default=False)
    perda_paladar = models.BooleanField(default=False)
    erupcao_cutanea = models.BooleanField(default=False)
    falta_ar = models.BooleanField(default=False)
    dor_peito = models.BooleanField(default=False)
    perda_fala = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)