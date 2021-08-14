# Generated by Django 3.1.7 on 2021-07-19 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210714_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('payment_status', models.CharField(choices=[('UNPAID', 'UNPAID'), ('PAID', 'PAID')], default='UNPAID', max_length=7)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.group')),
            ],
        ),
    ]
