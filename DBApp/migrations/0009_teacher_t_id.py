# Generated by Django 5.0.7 on 2024-09-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBApp', '0008_alter_student_s_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='T_id',
            field=models.IntegerField(null=True),
        ),
    ]
