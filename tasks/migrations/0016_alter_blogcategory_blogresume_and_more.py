# Generated by Django 4.2.5 on 2023-11-07 04:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0015_alter_about_aboutresume"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogcategory",
            name="blogResume",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="contact",
            name="contactResume",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="projectComplete",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="projectResume",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skillComplete",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skillsResume",
            field=models.TextField(),
        ),
    ]
