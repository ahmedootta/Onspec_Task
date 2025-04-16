from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    # Assume all fields are required
    class Meta:
        model = Candidate
        fields = '__all__'
