# Generated by Django 4.0.8 on 2023-06-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='spotlight', max_length=150, unique=True),
        ),
    ]
