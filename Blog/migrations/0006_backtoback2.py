# Generated by Django 3.0.6 on 2020-05-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_backtoback'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackToBack2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BackDate', models.DateField(auto_now_add=True)),
                ('BackIntro', models.CharField(blank=True, max_length=500)),
                ('BackDescription', models.CharField(max_length=2000)),
                ('BackUser', models.CharField(blank=True, max_length=200)),
                ('BackUserDiscipline', models.CharField(blank=True, max_length=200)),
                ('BackUniversity', models.CharField(blank=True, max_length=100)),
                ('BackVisibility', models.BooleanField(default=False)),
            ],
        ),
    ]