# Generated by Django 4.1.2 on 2024-06-12 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_entrada_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='imagen2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
