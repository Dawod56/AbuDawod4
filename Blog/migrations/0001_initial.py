# Generated by Django 3.0.6 on 2020-05-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('PostTitle', models.CharField(max_length=200)),
                ('PostImage', models.ImageField(upload_to='HomePostPics')),
                ('Description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ImportantLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkName', models.CharField(max_length=200)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('PhoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('Description', models.CharField(max_length=1000)),
                ('UserImage', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
