# Generated by Django 3.1.7 on 2021-03-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_modelo_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_texto_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_texto_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_texto_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_titulo_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_titulo_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='modelo_proyecto',
            name='etapa_titulo_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
