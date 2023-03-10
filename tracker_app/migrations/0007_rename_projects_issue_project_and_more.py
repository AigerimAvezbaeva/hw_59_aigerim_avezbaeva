# Generated by Django 4.1.6 on 2023-03-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0006_project_issue_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='projects',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
    ]