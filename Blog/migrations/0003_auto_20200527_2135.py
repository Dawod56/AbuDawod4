# Generated by Django 3.0.6 on 2020-05-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_headerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontents',
            name='PostImage',
            field=models.ImageField(blank=True, upload_to='HomePostPics'),
        ),
    ]
