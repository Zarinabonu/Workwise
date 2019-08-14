from rest_framework.serializers import ModelSerializer
from Project.models import Project


class Project_CreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('user', 'title', 'skills', 'price_from', 'price_to', 'description', 'category')
