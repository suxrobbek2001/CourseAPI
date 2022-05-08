from rest_framework.serializers import ModelSerializer

from .models import Teacher, Student, Course, Content, Video, Comment, Royxat


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RoyxatSerializer(ModelSerializer):
    class Meta:
        model = Royxat
        fields = '__all__'
