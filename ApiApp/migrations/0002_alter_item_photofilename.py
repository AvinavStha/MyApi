# Generated by Django 3.2 on 2021-04-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='PhotoFileName',
            field=models.ImageField(upload_to='', verbose_name='PhotoFileName/'),
        ),
    ]
