# Generated by Django 3.1.7 on 2021-07-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=200, verbose_name='email'),
        ),
    ]
