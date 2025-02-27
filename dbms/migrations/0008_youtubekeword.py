# Generated by Django 5.1 on 2024-08-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0007_alter_blogkeword_link_alter_blogkeword_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="YoutubeKeword",
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
                ("strd_dt", models.CharField(help_text="기준일자", max_length=8)),
                ("keword", models.CharField(help_text="검색어", max_length=500)),
                ("link", models.CharField(help_text="링크", max_length=500)),
                ("video_id", models.CharField(help_text="비디오ID", max_length=500)),
                ("main_text", models.TextField()),
                ("comment_author", models.CharField(help_text="댓글작성자", max_length=500)),
                ("ins_dt", models.CharField(help_text="입력일시", max_length=500)),
            ],
            options={
                "db_table": "dbms_youtube_keword",
            },
        ),
    ]
