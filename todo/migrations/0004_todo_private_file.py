# Generated by Django 5.0.3 on 2024-03-27 14:53

import private_storage.fields
import private_storage.storage.files
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='private_file',
            field=private_storage.fields.PrivateFileField(null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='private'),
        ),
    ]
