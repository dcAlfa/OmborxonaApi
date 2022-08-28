# Generated by Django 4.1 on 2022-08-27 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('brend', models.CharField(max_length=100)),
                ('kelgan_narx', models.PositiveSmallIntegerField()),
                ('sotuvdagi_narx', models.PositiveSmallIntegerField()),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ombor')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('dokon', models.CharField(max_length=100)),
                ('manzil', models.CharField(max_length=100)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ombor')),
            ],
        ),
    ]
