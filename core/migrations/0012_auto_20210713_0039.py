# Generated by Django 3.1.7 on 2021-07-13 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_fotosinfo_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Estado')),
                ('Estado', models.CharField(max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado'),
        ),
    ]
