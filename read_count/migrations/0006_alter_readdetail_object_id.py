# Generated by Django 4.2.2 on 2024-05-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("read_count", "0005_alter_readdetail_object_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="readdetail",
            name="object_id",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
