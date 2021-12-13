from rest_framework import serializers
from . import models
from ..base.services import delete_old_file
from ..oauth.serializer import AuthorSerializer


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class GenreSerializer(BaseSerializer):
    class Meta:
        model = models.Genre
        fields = ('id', 'name')


class LicenseSerializer(BaseSerializer):
    class Meta:
        model = models.License
        fields = ('id', 'text')


class AlbumSerializer(BaseSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'name', 'description', 'cover', 'private')

    def update(self, instance, validated_data):
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class CreateAuthorTrackSerializer(BaseSerializer):
    plays_count = serializers.IntegerField(read_only=True)
    download = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Track
        fields = (
            'id',
            'title',
            'license',
            'genre',
            'album',
            'link_of_author',
            'file',
            'create_at',
            'plays_count',
            'download',
            'private',
            'cover',
            'user'
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.file.path)
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class AuthorTrackSerializer(CreateAuthorTrackSerializer):
    license = LicenseSerializer()
    genre = GenreSerializer(many=True)
    album = AlbumSerializer()
    user = AuthorSerializer()


class CreatePlayListSerializer(BaseSerializer):
    class Meta:
        model = models.PlayList
        fields = ('id', 'title', 'cover', 'tracks')

    def update(self, instance, validated_data):
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class PlayListSerializer(CreatePlayListSerializer):
    tracks = AuthorTrackSerializer(many=True)


class CommentAuthorSerializer(serializers.ModelSerializer):
    """ Сериализация комментариев
    """

    class Meta:
        model = models.Comment
        fields = ('id', 'text', 'track')


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализация комментариев
    """
    user = AuthorSerializer()

    class Meta:
        model = models.Comment
        fields = ('id', 'text', 'user', 'track', 'create_at')


