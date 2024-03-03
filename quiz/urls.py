
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename="category")
router.register(r'question', QuestionViewSet, basename="question")

urlpatterns = [
    path('',include(router.urls)),
    path("question-bulk-create/", QuestionListAPIView.as_view())
]


