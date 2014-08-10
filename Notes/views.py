from django.contrib.auth.models import User
from rest_framework import generics, permissions
from Notes.models import Note
from Notes.serializers import NoteSerializer, UserSerializer
from Notes.permissions import IsOwner


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return Note.objects.filter(author__exact=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
