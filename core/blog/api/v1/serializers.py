from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile, User
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_path = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    #category = serializers.SlugRelatedField(many=False,slug_field='name', queryset = Category.objects.all() )
    class Meta:
        model = Post
        fields = ["id","author","image","title", "content","snippet","category","status","absolute_url","relative_path","created_date","published_date",
            ]
        read_only_fields = ['author']
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] =CategorySerializer(instance.category).data
        rep.pop('snippet', None)
        return rep

    def create(self, validated_data):
        user = User.objects.get(id = self.context.get('request').user.id)
        validated_data['author'] = Profile.objects.get(user = user )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)