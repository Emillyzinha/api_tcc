# Generated by Django 4.2.4 on 2023-09-19 17:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_treinamentos_delete_treinamento1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treinamentos',
            name='imagem',
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id_imagem', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('imagem', models.ImageField(upload_to='media')),
                ('id_imagem_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.treinamentos')),
            ],
        ),
    ]
