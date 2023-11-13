# Generated by Django 4.2.3 on 2023-07-31 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_perguntasfuturas_alter_luiza_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luiza',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8b620205-26c8-4640-8a67-469c15ef276d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='resposta',
            field=models.TextField(max_length=500, null=True),
        ),
    ]