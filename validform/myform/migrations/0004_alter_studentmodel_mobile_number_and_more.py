# Generated by Django 5.1.1 on 2024-10-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myform", "0003_alter_studentmodel_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmodel",
            name="mobile_number",
            field=models.BigIntegerField(default=9565851570),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="roll_number",
            field=models.IntegerField(default=121),
        ),
    ]
