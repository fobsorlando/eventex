# Generated by Django 2.0.6 on 2018-08-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'palestrante', 'verbose_name_plural': 'palestrantes'},
        ),
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.URLField(verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.URLField(blank=True, verbose_name='WebSite'),
        ),
    ]
