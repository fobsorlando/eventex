# Generated by Django 2.0.6 on 2018-08-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180820_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='Inicio')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='Palestrantes')),
            ],
            options={
                'verbose_name_plural': 'palestras',
                'verbose_name': 'palestra',
                'abstract': False,
            },
        ),
    ]