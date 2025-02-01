# Generated by Django 5.1 on 2024-08-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0006_blogkeword"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogkeword",
            name="link",
            field=models.CharField(help_text="링크", max_length=500),
        ),
        migrations.AlterField(
            model_name="blogkeword",
            name="title",
            field=models.CharField(help_text="제목", max_length=500),
        ),
    ]
