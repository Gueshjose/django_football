# Generated by Django 4.2.2 on 2023-06-20 11:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Europe', 'Europe'), ('Asie', 'Asie'), ('Afrique', 'Afrique'), ('Amerique', 'Amerique'), ('Oceanie', 'Oceanie')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(choices=[('Attaquant', 'Attaquant'), ('Millieu', 'Millieu'), ('Défenseur', 'Défenseur'), ('Gardien', 'Gardien'), ('Remplaçant', 'Remplaçant')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ville', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=20)),
                ('maxATT', models.IntegerField()),
                ('maxMID', models.IntegerField()),
                ('maxDEF', models.IntegerField()),
                ('maxG', models.IntegerField()),
                ('maxREM', models.IntegerField()),
                ('logo', models.ImageField(upload_to='img/')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercato.continent')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(35)])),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=1)),
                ('country', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='img/')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercato.role')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercato.team')),
            ],
        ),
    ]
