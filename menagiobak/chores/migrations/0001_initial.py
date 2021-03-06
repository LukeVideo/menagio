# Generated by Django 3.1.5 on 2021-01-12 15:33

import chores.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(default='default place', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_points', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('task_description', models.CharField(default='default task_description', max_length=600)),
                ('task_frequency', models.IntegerField(default=7, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(365)])),
                ('task_place', models.ForeignKey(default=chores.models.get_default_task_place, on_delete=django.db.models.deletion.CASCADE, to='chores.place')),
            ],
        ),
    ]
