# Generated by Django 4.0.4 on 2022-05-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_cadeira_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='semestre',
            field=models.IntegerField(choices=[(1, 'semestre 1'), (2, '2º semestre 2')], default=1),
        ),
    ]