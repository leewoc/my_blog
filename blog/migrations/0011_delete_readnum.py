# Generated by Django 4.2.2 on 2024-05-30 23:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_rename_read_readnum_read_num"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ReadNum",
        ),
    ]
