# programs/serializers.py
from rest_framework import serializers
from .models import Program
from partners.models import Partner


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
        existing_partner = Partner.objects.filter(id=validated_data["partner_id"]).first()
        if not existing_partner:
            errmsg = str("There is no Partner with id: %s, returning Null Program" % validated_data["partner_id"])
            return null_program

        program = Program.objects.create(**validated_data)
        program.partner_id = validated_data["partner_id"]

        try:
            program.save()
            return program
        except Exception as exception:
            errmsg = "Unexpected error when trying to save: " + str(exception)
            return null_program
