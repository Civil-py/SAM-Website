# Generated by Django 5.0.3 on 2024-06-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userallocation',
            old_name='software_id',
            new_name='software',
        ),
    ]