from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from Job.models import Post, Category, Time, Comment, Notification


class JobCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'skills', 'price', 'description')

    def create(self, validated_data):
        print('POST ',validated_data)
        request = self.context['request']
        p = Post(**validated_data)
        t = Time.objects.get(full_time=request.data.get('time'))
        c = Category.objects.get(categories=request.data.get('category'))
        u = User.objects.get(username=request.user.username)
        print('USERNAME :', u)
        p.category = c
        p.time = t
        p.user = u
        p.save()
        return p


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)

    def create(self, validated_data):
        c = Comment(**validated_data)
        request = self.context['request']
        u = User.objects.get(username=request.user.username)
        p = Post.objects.get(id=request.POST['post'])
        c.post = p
        c.user = u
        c.save()
        return c


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)

    def create(self, validated_data):
        c = Comment(**validated_data)
        request = self.context['request']
        u = User.objects.get(username=request.user.username)
        # rep = Comment.objects.get()
        p_c = Comment.objects.get(id=request.POST['parent_id'])
        # p = Post.objects.get(id=request.POST['post'])
        c.reply_is = True
        c.reply = p_c
        # c.post = p
        c.user = u
        c.save()
        return c


class LikesSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        p = Post.objects.get(id=request.POST['post'])
        p.likes.add(request.user)
        print('LIKES ',p)

        return p


class SavedSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        # u = User.objects.get(username=request.user.username)
        p = Post.objects.get(id=request.POST['post'])

        p.saved.add(request.user)

        return p


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        p = Post.objects.get(id=request.POST['post'])
        n = Notification.objects.create(post=p, sender=request.user, receiver=p.user)
        n.save()

        return n

class ViewSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        p = Post.objects.get(id=request.POST['post'])
        p.view.add(request.user)

        return p







