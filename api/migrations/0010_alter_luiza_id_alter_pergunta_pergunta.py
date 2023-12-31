# Generated by Django 4.2.3 on 2023-07-31 16:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_luiza_id_alter_resposta_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luiza',
            name='id',
            field=models.UUIDField(default=uuid.UUID('69fb9759-4217-4145-9ef3-6307da764c06'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='pergunta',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
