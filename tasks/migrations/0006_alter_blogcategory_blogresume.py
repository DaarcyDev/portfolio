# Generated by Django 4.2.5 on 2023-10-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_blogcategory_blogfile_skillsimages_delete_blog_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogcategory",
            name="blogResume",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]