# Generated by Django 5.1 on 2024-08-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0011_kakaotalk"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicAptTrade",
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
                ("sgg_cd", models.CharField(help_text="법정동시군구코드", max_length=500)),
                ("road_nm", models.CharField(help_text="도로명", max_length=500)),
                ("apt_nm", models.CharField(help_text="아파트명", max_length=500)),
                ("excul_use_area", models.CharField(help_text="전용면적", max_length=500)),
                ("deal_year", models.CharField(help_text="계약년도", max_length=50)),
                ("deal_amount", models.CharField(help_text="거래금액(만원)", max_length=50)),
                ("floor", models.CharField(help_text="층", max_length=50)),
                ("build_year", models.CharField(help_text="건축년도", max_length=50)),
                ("seller_gubun", models.CharField(help_text="매도자구분", max_length=50)),
                ("buyer_gubun", models.CharField(help_text="매수자구분", max_length=50)),
                ("ins_dt", models.CharField(help_text="입력일시", max_length=50)),
            ],
            options={
                "db_table": "dbms_public_apt_trade",
            },
        ),
    ]
