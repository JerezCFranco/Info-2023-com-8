# Generated by Django 4.2.2 on 2023-07-20 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_post_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resumen',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
