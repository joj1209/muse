# Generated by Django 5.1 on 2024-08-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0013_kmaneighborhoodweather"),
    ]

    operations = [
        migrations.CreateModel(
            name="JejuApiFloatingPopulation",
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
                ("regist_dt", models.CharField(help_text="등록일자", max_length=8)),
                ("city", models.CharField(help_text="시군구", max_length=500)),
                ("emd", models.CharField(help_text="읍면동", max_length=500)),
                ("gender", models.CharField(help_text="성별", max_length=500)),
                ("age_group", models.CharField(help_text="연령대", max_length=500)),
                ("resd_pop", models.CharField(help_text="거주인구", max_length=50)),
                ("work_pop", models.CharField(help_text="근무인구", max_length=50)),
                ("visit_pop", models.CharField(help_text="방문자수", max_length=50)),
                ("ins_dt", models.CharField(help_text="입력일시", max_length=50)),
            ],
            options={
                "db_table": "dbms_jeju_api_floating_population",
            },
        ),
        migrations.CreateModel(
            name="SeoulApiSpopFornLongResdJachi",
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
                ("stdr_de_id", models.CharField(help_text="기준일ID", max_length=500)),
                ("tmzon_pd_se", models.CharField(help_text="시간대구분", max_length=500)),
                ("adstrd_code_se", models.CharField(help_text="자치구코드", max_length=500)),
                ("tot_lvpop_co", models.CharField(help_text="총생활인구수", max_length=500)),
                (
                    "china_staypop_co",
                    models.CharField(help_text="중국인체류인구수", max_length=500),
                ),
                (
                    "etc_staypop_co",
                    models.CharField(help_text="중국외외국인체류인구수", max_length=500),
                ),
                ("ins_dt", models.CharField(help_text="입력일시", max_length=50)),
            ],
            options={
                "db_table": "dbms_seoul_api_spop_forn_long_resd_jachi",
            },
        ),
    ]
