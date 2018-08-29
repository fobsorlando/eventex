from django.db import models
from django.shortcuts import resolve_url as r

# Create your models here.
from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('Nome',max_length=255)
    slug = models.SlugField('Slug')
    photo = models.URLField('Foto')
    website = models.URLField('WebSite', blank=True)
    description = models.TextField('Descrição', blank=True)



    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

class Contact(models.Model):
    EMAIL='E'
    PHONE='P'

    KINDS = (
        (EMAIL, 'E-mail'),
        (PHONE, 'Telefone'),
    )

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='Palestrante')
    kind = models.CharField('Tipo', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value

class Activity(models.Model):
    title = models.CharField('Título',max_length=200)
    start = models.TimeField('Inicio', blank=True, null=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Palestrantes', blank=True )

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name = "palestra"
        verbose_name_plural="palestras"


    def __str__(self):
        return self.title

class Talk(Activity):
    pass

class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"





