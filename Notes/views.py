from rest_framework import authentication, generics, permissions
from oauth2_provider.ext.rest_framework import TokenHasScope
from Notes.models import Note
from Notes.serializers import NoteSerializer
from Notes.permissions import IsOwner


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    authentication_classes = (authentication.oauth2_provider,)
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    required_scopes = ('notes',)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    authentication_classes = (authentication.oauth2_provider,)
    permission_classes = (permissions.IsAuthenticated, IsOwner, TokenHasScope,)
    required_scopes = ('notes',)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)
