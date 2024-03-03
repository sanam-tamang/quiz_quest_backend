from django.db import models
from uuid import uuid4
class BaseModel(models.Model):
    id = models.UUIDField(default= uuid4, serialize=True, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True) 
      
    class Meta: 
        abstract = True 

class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True, default= None)
    def __str__(self) -> str:
        return self.name


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.question_text
    


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "options")
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.option_text
