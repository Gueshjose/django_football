# Generated by Django 4.2.2 on 2023-06-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercato', '0004_alter_player_photo_alter_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='img',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
    ]
