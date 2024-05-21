from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from . models import Note
from . serializers import NoteSerializer
from .filters import NoteFilter


class NonPrimaryKeyNoteView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notes = Note.objects.filter(
            owner=request.user).select_related('category')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoteSerializer(
            data=request.data, context={
                'current_user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrimaryKeyNoteView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        current_note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(
            current_note, data=request.data, context={
                'current_user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        current_note = Note.objects.get(pk=pk)
        current_note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivedNotesView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notes = Note.objects.select_related(
            "category").filter(is_archived=True)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        rest_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'created_at',
        'words_in_note',
        'words_in_note',
        'unique_words_in_note']
    filterset_class = NoteFilter

    def get_queryset(self):
        current_user = self.request.user
        return Note.objects.select_related(
            "category").filter(owner=current_user)
