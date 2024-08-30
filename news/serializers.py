from rest_framework.serializers import ModelSerializer
from .models import News
from authentication.models import Author


class AuthorNewsSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "username", "bio", "subtitle", "image"]


class NewsSerializer(ModelSerializer):
    author = AuthorNewsSerializer(read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "banner",
            "content",
            "created_time",
            "updated_time",
            "author",
        ]
