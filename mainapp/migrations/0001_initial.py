# Generated by Django 3.1.7 on 2021-07-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('specification', models.CharField(choices=[('FRONTEND', 'FRONTEND'), ('BACKEND', 'BACKEND'), ('ANDROID', 'ANDROID'), ('IOS', 'IOS'), ('FLUTTER', 'FLUTTER'), ('REACT-N', 'REACT-N'), ('DESKTOP', 'DESKTOP'), ('FULLSTACK', 'FULLSTACK')], default='FRONTEND', max_length=10)),
                ('level', models.CharField(choices=[('JUNIOR', 'JUNIOR'), ('MIDDLE', 'MIDDLE'), ('SENIOR', 'SENIOR')], default='JUNIOR', max_length=7)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
    ]
