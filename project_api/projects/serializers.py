# project/serializers.py
from rest_framework import serializers
from .models import Project
from programs.models import Program


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'program_id', )


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'program_id', )

    program_id = serializers.IntegerField()

    def create(self, validated_data):

        null_project = {
            "project_name": None,
            "program_id": None,
        }

        # Check if a matching program with program_id exists
        existing_program = Program.objects.filter(
            id=validated_data["program_id"]
        ).first()
        errmsg = \
            "There is no Program with id: " + \
            str(validated_data["program_id"]) + \
            ", returning Null Project"
        if not existing_program:
            return null_project

        project = Project.objects.create(**validated_data)
        project.program_id = validated_data["program_id"]

        try:
            project.save()
            return project
        except Exception as exception:
            errmsg = "Unexpected Exception: " + str(exception)
            return null_project
