# Generated by Django 5.0.7 on 2024-07-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_qdjgyp', upload_to='images/'),
        ),
    ]
