# Generated by Django 4.0.8 on 2023-05-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='teaser',
            field=models.TextField(blank=True, help_text='If left blank, it will be populated with a portion of the body.', max_length=100, null=True),
        ),
    ]