# Generated by Django 4.1.2 on 2022-11-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0003_haga_su_pedido_tipo_de_relleno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haga_su_pedido',
            name='cantidad_de_personas',
            field=models.IntegerField(null=True),
        ),
    ]
