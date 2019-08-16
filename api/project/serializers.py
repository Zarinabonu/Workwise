from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from Project.models import Project, Category


class Project_CreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'skills', 'price_from', 'price_to', 'description')

    def create(self, validated_data):
        print('POST ', validated_data)
        request = self.context['request']
        p = Project(**validated_data)
        c = Category.objects.get(categories=request.data.get('category'))
        u = User.objects.get(username=request.user.username)
        p.user = u
        p.category = c
        p.save()
        return p
