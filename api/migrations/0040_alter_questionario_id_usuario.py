# Generated by Django 4.2.4 on 2023-10-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_questionario_questao_5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='id_usuario',
            field=models.EmailField(max_length=254),
        ),
    ]
