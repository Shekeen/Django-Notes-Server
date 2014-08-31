from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')

    class Meta:
        model = Note
        fields = ('text', 'add_time', 'last_update',)
        read_only_fields = ('add_time', 'last_update',)
