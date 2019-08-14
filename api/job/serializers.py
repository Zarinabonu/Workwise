from rest_framework.serializers import ModelSerializer
from Job.models import Post, Category


class JobCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'skills', 'price', 'description', 'category', 'time')

    # def create(self, validated_data):
    #     print('POST ',validated_data)
    #     p = Post(**validated_data)
    #     c = Category.objects.get()
    #     p.category = c
    #     p.save()
    #     return p



