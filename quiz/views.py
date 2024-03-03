
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from quiz_quest_core.custom_pagination import QuizResultsSetPagination
import random
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuizResultsSetPagination
    def list(self, request):
        category_id = request.query_params.get("category_id")
        try:
            category = Category.objects.get(pk = category_id)
            questions = list(Question.objects.filter(category = category))
            random.shuffle(questions)
     
            paginated_questions = self.paginate_queryset(questions)
            serializer = QuestionSerializer(paginated_questions, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist: 
            questions = list(Question.objects.all())
            random.shuffle(questions)
            paginated_questions = self.paginate_queryset(questions)
            serializer = QuestionSerializer(paginated_questions, many=True)
            return Response(serializer.data)





#This is not right way to bulk create for this project its fine
class QuestionListAPIView(APIView):
    def post(self, request):
        message = "Success"
        for data in request.data:
            serializer = QuestionSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else: 
                message = "Error"
        return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)