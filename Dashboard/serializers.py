from rest_framework import serializers
from .models import FunctionalArea, IndustryType



class IndustryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryType
        fields = ['id', 'name']
        # Optional: You can exclude 'id' field if you don't want to include it in the serialized data
        # exclude = ['id']

    # Optional: You can add extra validation or customization here if needed
    def validate_name(self, value):
        # Add custom validation logic for the 'name' field if necessary
        return value

class FunctionalAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FunctionalArea
        fields = [ 'name']
        # Optional: You can exclude 'id' field if you don't want to include it in the serialized data
        # exclude = ['id']

    # Optional: You can add extra validation or customization here if needed
    def validate_name(self, value):
        # Add custom validation logic for the 'name' field if necessary
        return value