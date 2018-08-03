from django.db import models

from eventex.subscriptions.validators  import validate_cpf


class Subscription(models.Model):
    name = models.CharField('Nome do Participante',max_length=100)
    cpf = models.CharField('C.P.F.',max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-Mail', blank=True)
    phone = models.CharField('Tefone',max_length=20, blank=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    paid = models.BooleanField('Pago',default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name