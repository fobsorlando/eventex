from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome do Participante',max_length=100)
    cpf = models.CharField('C.P.F.',max_length=11)
    email = models.EmailField('E-Mail')
    phone = models.CharField('Tefone',max_length=20)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name