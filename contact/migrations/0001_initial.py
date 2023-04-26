# Generated by Django 3.2.12 on 2022-03-21 08:46

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "meeting_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("monthly_meeting", "Monthly Meeting"),
                            ("quarterly_meeting", "Quarterly Meeting"),
                            ("worship_group", "Worship Group"),
                            ("yearly_meeting", "Yearly Meeting"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "description",
                    wagtail.fields.RichTextField(blank=True, null=True),
                ),
                ("website", models.URLField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=64, null=True)),
                ("civicrm_id", models.IntegerField(blank=True, null=True)),
                ("drupal_author_id", models.IntegerField(blank=True, null=True)),
                (
                    "drupal_library_author_id",
                    models.IntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "meeting",
                "ordering": ["title"],
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MeetingIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("website", models.URLField(blank=True, null=True)),
                ("civicrm_id", models.IntegerField(blank=True, null=True)),
                ("drupal_author_id", models.IntegerField(blank=True, null=True)),
                (
                    "drupal_library_author_id",
                    models.IntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "organization",
                "ordering": ["title"],
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="OrganizationIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "given_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Enter the given name for a person.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "family_name",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                ("drupal_author_id", models.IntegerField(blank=True, null=True)),
                (
                    "drupal_library_author_id",
                    models.IntegerField(blank=True, null=True),
                ),
                ("civicrm_id", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "people",
                "db_table": "person",
                "ordering": ["title"],
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PersonIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MeetingWorshipTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "worship_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("first_day_worship", "First day worship"),
                            ("first_day_worship_2nd", "First day worship, 2nd"),
                            ("business_meeting", "Business meeting"),
                            ("other_regular_meeting", "Other regular meeting"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("worship_time", models.CharField(max_length=255)),
                (
                    "meeting",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="worship_times",
                        to="contact.meeting",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MeetingPresidingClerk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "meeting",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="presiding_clerks",
                        to="contact.meeting",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clerk_of",
                        to="contact.person",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MeetingAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "street_address",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "extended_address",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "po_box_number",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="P.O. Box, if relevant",
                        max_length=32,
                    ),
                ),
                (
                    "locality",
                    models.CharField(
                        blank=True,
                        help_text="Locality or city",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="State or region",
                        max_length=255,
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        help_text="Postal code (or zipcode)",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, default="United States", max_length=255, null=True
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        choices=[("mailing", "Mailing"), ("worship", "Worship")],
                        max_length=255,
                    ),
                ),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="contact.meeting",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
