# Generated by Django 4.2.2 on 2023-06-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercato', '0004_alter_player_photo_alter_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='composition',
            field=models.CharField(choices=[('M', 'Masculine'), ('F', 'Feminine'), ('X', 'Mixte')], default='X', max_length=1),
        ),
    ]
