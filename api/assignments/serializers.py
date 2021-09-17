from rest_framework import serializers
from core.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        extra_kwargs = {
            'classroom': {
                'required': False
            }
        }
