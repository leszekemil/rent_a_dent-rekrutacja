# Generated by Django 3.1.4 on 2020-12-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_dent', '0003_auto_20201230_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='type',
            field=models.CharField(choices=[('KONS', 'Konsultacja'), ('INTER', 'Interwencja'), ('OPERA', 'Operacja')], max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='visit',
            unique_together={('day', 'hour', 'type')},
        ),
    ]
