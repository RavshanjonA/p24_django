# Generated by Django 5.0.7 on 2024-07-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_speciality_options_alter_speciality_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(related_name='teachers', to='course.subject'),
        ),
    ]
