from rest_framework import serializers
from rent_a_dent.models import Visit, VISIT_TYPE


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = "__all__"