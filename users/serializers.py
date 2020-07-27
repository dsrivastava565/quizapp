from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


models.CustomUser._meta.get_field('email')._unique = True

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ('id','question', 'option1','option2','option3','option4','AddedBy','answer')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = '__all__'

class QuizquestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestions
        fields = '__all__'
class QuizSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizSubmission
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
