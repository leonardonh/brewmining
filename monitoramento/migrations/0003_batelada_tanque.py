# Generated by Django 2.0 on 2017-12-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoramento', '0002_remove_medida_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='batelada',
            name='tanque',
            field=models.IntegerField(default=0),
        ),
    ]
