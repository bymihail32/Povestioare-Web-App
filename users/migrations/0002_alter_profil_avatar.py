# Generated by Django 4.1.3 on 2022-12-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(default='prima.jpg', upload_to='profile_images'),
        ),
    ]
