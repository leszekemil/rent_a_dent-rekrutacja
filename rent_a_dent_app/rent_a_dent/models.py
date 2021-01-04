from django.db import models
from django.core.exceptions import ValidationError
import datetime
from phone_field import PhoneField
from django.core.validators import RegexValidator

# Create your models here.

AVAILABLE_HOURS = (
    ("8-9", "8:00 - 9:00"),
    ("9-10", "9:00 - 10:00"),
    ("10-11", "10:00 - 11:00"),
    ("11-12", "11:00 - 12:00"),
    ("12-13", "12:00 - 13:00"),
    ("13-14", "13:00 - 14:00"),
    ("14-15", "14:00 - 15:00"),
    ("15-16", "15:00 - 16:00"),
)

VISIT_TYPE = (
    ("Konsultacja", "Konsultacja"),
    ("Interwencja", "Interwencja"),
    ("Operacja", "Operacja"),
)


def no_pass_date(value):
    today = datetime.date.today()
    if value < today:
        raise ValidationError('Proszę zarezerować wizytę w przyszłości.')


class Visit(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    mail = models.EmailField(max_length=254, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Numer telefonu musi zawierać się w formacie: '+999999999'.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    day = models.DateField(validators=[no_pass_date])
    hour = models.CharField(max_length=64, choices=AVAILABLE_HOURS)
    type = models.CharField(max_length=64, choices=VISIT_TYPE)

    def __str__(self):
        return self.day

    def get_detail_url(self):
        return f'/visit/{self.id}'

    def get_edit_url(self):
        return f'/visit/update/{self.id}'

    def del_url(self):
        return f"/visit/delete/{self.id}"

    class Meta:
        unique_together = ("day", "hour", "type")

    @staticmethod
    def visits_amount():
        return Visit.objects.all().count()
