# Generated by Django 3.1.4 on 2020-12-30 13:47

from django.db import migrations, models
import rent_a_dent.models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_dent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='day',
            field=models.DateField(help_text='Podaj datę wizyty', validators=[rent_a_dent.models.no_pass_date]),
        ),
        migrations.AlterField(
            model_name='visit',
            name='hour',
            field=models.DateTimeField(choices=[('8-9', '8:00 - 9:00'), ('9-10', '9:00 - 10:00'), ('10-11', '10:00 - 11:00'), ('11-12', '11:00 - 12:00'), ('12-13', '12:00 - 13:00'), ('13-14', '13:00 - 14:00'), ('14-15', '14:00 - 15:00'), ('15-16', '15:00 - 16:00')], help_text='Podaj godzinę wizyty'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='type',
            field=models.CharField(choices=[('KONSU', 'Konsultacja'), ('INTER', 'Interwencja'), ('OPERA', 'Operacja')], max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='visit',
            unique_together={('day', 'hour', 'type')},
        ),
    ]
