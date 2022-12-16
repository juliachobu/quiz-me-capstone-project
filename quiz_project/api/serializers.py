from rest_framework import serializers
from django.contrib.auth import get_user_model

from quiz_me_app.models import Question, Choice, Result

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text', 'question')


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'text', 'choices')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'correct_answer', 'question', 'user',)


class UserSerializer(serializers.ModelSerializer):
    post_detail = ResultSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'post_detail')
        
# class NestedResultSerializer(serializers.ModelSerializer):
#     post_detail = UserSerializer(many=True, read_only=True)
#     class Meta:
#         model = Result
#         fields = ('id', 'correct_answer', 'question', 'user', 'post_detail')

