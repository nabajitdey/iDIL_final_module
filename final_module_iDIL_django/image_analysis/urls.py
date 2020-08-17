from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
from rest_framework import routers

urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.index, name='index'),
    path('image_upload/', hotel_image_view, name = 'image_upload'),
    path('success/', success, name = 'success'),
    path('sort_objects/', ObjectsDbUploadViewSet.as_view()),
    path('image_detection/', ImageDetectionViewSet.as_view()),
    path('affirmation_question/', AffirmationQuestionViewSet.as_view()),
    path('list_question/', ListQuestionViewSet.as_view()),
    path('text_analysis/', TextAnalysisViewSet.as_view()),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)