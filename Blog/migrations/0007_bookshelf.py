# Generated by Django 3.0.6 on 2020-05-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_backtoback2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=500)),
                ('Writer', models.CharField(blank=True, max_length=500)),
                ('BookLink', models.URLField(max_length=2000)),
                ('BookCategory', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
