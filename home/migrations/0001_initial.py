# Generated by Django 4.0.8 on 2023-05-24 10:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailpod', '0001_initial'),
        ('blogs', '0002_rename_image_blog_display_image_remove_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageFeaturedPodcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailpod.podcastpage')),
                ('home_page', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_podcasts', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageFeaturedBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blogs.blog')),
                ('home_page', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_blogs', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
