# Generated by Django 4.2.2 on 2023-06-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercato', '0003_tactics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
