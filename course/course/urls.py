from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from courseapp.views import TeacherLC, TeacherRUD, StudentLC, StudentRUD, CourseLC, CourseRUD, ContentLC, \
    ContentRUD, VideoLC, VideoRUD, CommentLC, CommentRUD, RoyxatLC, RoyxatRUD

from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
   openapi.Info(
      title="Course API",
      default_version='v1',
      description="Course API",
      contact=openapi.Contact("Sukhrobbek Mukhammadjonov <surobbekmuxammadjonov2gmail.com>, <+998993930242>"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TeacherLC.as_view()),
    path('/<int:pk>/', TeacherRUD.as_view()),

    path('student/', StudentLC.as_view()),
    path('student/<int:pk>/', TeacherRUD.as_view()),

    path('course/', CourseLC.as_view()),
    path('course/<int:pk>/', CourseRUD.as_view()),

    path('content/', ContentLC.as_view()),
    path('content/<int:pk>/', ContentRUD.as_view()),

    path('video/', VideoLC.as_view()),
    path('video/<int:pk>/', VideoRUD.as_view()),

    path('comment/', CommentLC.as_view()),
    path('comment/<int:pk>/', CommentRUD.as_view()),

    path('royxat/', RoyxatLC.as_view()),
    path('royxat/<int:pk>/', RoyxatRUD.as_view()),

    #dokumentatsiya
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),

    path('get-token/', obtain_auth_token),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)