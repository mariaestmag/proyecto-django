# Generated by Django 3.2.8 on 2021-11-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Libro'},
        ),
        migrations.AddField(
            model_name='book',
            name='fecha',
            field=models.DateField(blank=True, help_text='Fecha de publicacion', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='catalogo.Genre'),
        ),
    ]
