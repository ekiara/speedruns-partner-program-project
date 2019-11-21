# programs/serializers.py
from rest_framework import serializers
from .models import Program
from partners.helpers import get_partner


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id', 'program_name', 'program_code', 'project_count',
                  'partner_id', )


class ProgramCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id', 'program_name', 'program_code', 'project_count',
                  'partner_id', )

    partner_id = serializers.IntegerField()

    def create(self, validated_data):

        null_program = {
            "program_name": None,
            "program_code": None,
            "partner_id": None,
        }

        # Check if a matching partner with partner_id exists
        # existing_partner = Partner.objects.filter(id=validated_data['partner_id']).first()
        existing_partner = get_partner(partner_id=validated_data['partner_id'])
        if not existing_partner:
            errmsg = ("There is no Partner with id: " +
                      str(validated_data["partner_id"]) +
                      ", returning Null Program Object.")
            return null_program

        # If we're here then a partner with partner_id exists and we can
        # proceed.
        program = Program.objects.create(**validated_data)
        program.partner_id = validated_data['partner_id']

        try:
            program.save()
            return program
        except Exception as exception:
            errmsg = "Unexpected Exception: " + str(exception)
            return null_program
