# Generated by Django 5.0.1 on 2024-02-15 19:45

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_examplemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
