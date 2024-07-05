# Generated by Django 5.0.6 on 2024-06-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ammunation', '0007_alter_arma_calibre_alter_perfil_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='calibre',
             field=models.CharField(choices=[('Pistola', 'Pistola'), ('Escopeta', 'Escopeta'), ('Subfusil', 'Subfusil'), ('Fusil', 'Fusil'), ('Francotirador', 'Francotirador')], max_length=13),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='ciudad',
            field=models.CharField(choices=[('Curanilahue', 'Curanilahue'), ('Concepción', 'Concepción'), ('Colina', 'Colina')], max_length=20),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('ENVIADO', 'ENVIADO'), ('EN PREPARACIÓN', 'EN PREPARACIÓN'), ('PREPARADO', 'PREPARADO'), ('ENTREGADO', 'ENTREGADO')], default='EN PREPARACIÓN', max_length=30),
        ),
    ]
