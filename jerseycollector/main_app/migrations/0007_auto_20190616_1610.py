# Generated by Django 2.2.2 on 2019-06-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20190616_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammate',
            name='jersey',
        ),
        migrations.AddField(
            model_name='jersey',
            name='teammate',
            field=models.ManyToManyField(to='main_app.Teammate'),
        ),
    ]