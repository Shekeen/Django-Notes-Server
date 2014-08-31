from rest_framework import generics, permissions
from oauth2_provider.ext.rest_framework import TokenHasScope
from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    required_scopes = ('notes',)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    required_scopes = ('notes',)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)
