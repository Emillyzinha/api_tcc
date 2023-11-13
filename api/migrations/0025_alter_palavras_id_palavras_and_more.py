# Generated by Django 4.2.4 on 2023-08-04 13:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_palavras_id_palavras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palavras',
            name='id_palavras',
            field=models.UUIDField(default=uuid.UUID('03559a11-eefa-465c-8654-320359aa78b7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='id_resposta',
            field=models.UUIDField(default=uuid.UUID('e98ee37c-bdb1-4459-8755-d05d612e2944'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.UUIDField(default=uuid.UUID('92680630-068e-4a3d-816b-48d98547db53'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.TextField(default=uuid.UUID('43c4ba33-eaef-4eef-9e55-14684bf14d28'), max_length=100),
        ),
    ]
