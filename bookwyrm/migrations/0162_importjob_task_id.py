# Generated by Django 3.2.15 on 2022-11-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0161_alter_importjob_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="importjob",
            name="task_id",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
