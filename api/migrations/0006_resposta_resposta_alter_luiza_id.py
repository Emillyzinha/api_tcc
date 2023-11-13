# Generated by Django 4.2.3 on 2023-07-20 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_resposta_resposta_alter_luiza_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='resposta',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='luiza',
            name='id',
            field=models.UUIDField(default=uuid.UUID('501f5e52-62fe-4966-9721-f3df422af45f'), primary_key=True, serialize=False),
        ),
    ]