
from rest_framework import serializers
from .models import *
import random

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'option_text', 'is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
  
    class Meta:
        model = Question
        fields = '__all__'
    
    def create(self, validated_data):
        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
        return question

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        options_data = validated_data.get('options')
        print("&&&&&&&&")
        print(validated_data)
        print(instance)
        if options_data:
            print("Iaminside if")
            for option_data in options_data:
                print("###Ilooop $$$$$$$$$$$%%%%%%%%%")
                option_id = option_data.get('id')
                print("*************************")

                print(option_data)
                print("*************************")
                if option_id:
                    print("!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    option = Option.objects.get(pk=option_id)
                    option.option_text = option_data.get('option_text', option.option_text)
                    option.is_correct = option_data.get('is_correct', option.is_correct)
                    option.save()
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                    # Option.objects.create(question=instance, **option_data)
        print("###Iamoutsideside if")
        return instance
#making field to post as id and read as whole data
    def to_representation(self, value):
        data = super().to_representation(value)  
        category_serializer = CategorySerializer(value.category)
        data['category'] = category_serializer.data['name']
        option_serializer =  OptionSerializer(value.options, many=True)
        option_data =    option_serializer.data
        random.shuffle(option_data)
        data['options'] = option_data

        return data
    


