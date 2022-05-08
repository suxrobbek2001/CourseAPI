from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Teacher, Student, Course, Content, Video, Comment, Royxat
from .serializers import TeacherSerializer, StudentSerializer, CourseSerializer, ContentSerializer, VideoSerializer, \
    CommentSerializer, RoyxatSerializer


class TeacherLC(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teachers = Teacher.objects.filter(user=self.request.user)
        return teachers


class TeacherRUD(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teachers = Teacher.objects.filter(user=self.request.user)
        return teachers

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        students = Student.objects.filter(user=self.request.user)
        return students

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        students = Student.objects.filter(user=self.request.user)
        return students

class CourseLC(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [SearchFilter, ]
    search_fields = ["id", "name", ]
    # def get_queryset(self):
    #     course = Course.objects.all()
    #     soz = self.request.query_params.get("search")
    #     if soz is not None:
    #         course = Course.objects.annotate(
    #             similarity=TrigramSimilarity("name", soz)
    #         ).filter(similarity__gte=0.4).order_by("-similarity")
    #     return course




class CourseRUD(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["id", "name", ]
    # def get_queryset(self):
    #     course = Course.objects.all()
    #     soz = self.request.query_params.get("search")
    #     if soz is not None:
    #         course = Course.objects.annotate(
    #             similarity=TrigramSimilarity("name", soz)
    #         ).filter(similarity__gte=0.4).order_by("-similarity")
    #     return course
    #


class ContentLC(ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class VideoLC(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRUD(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentLC(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RoyxatLC(ListCreateAPIView):
    queryset = Royxat.objects.all()
    serializer_class = RoyxatSerializer


class RoyxatRUD(RetrieveUpdateDestroyAPIView):
    queryset = Royxat.objects.all()
    serializer_class = RoyxatSerializer