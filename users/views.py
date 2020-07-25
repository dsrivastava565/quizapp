from rest_framework import generics

from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
        
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": serializer.data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        data = [{'auth':request,'user':user}]
        print(request);
        return super(LoginAPI, self).post(request, format=None)

class QuestionAPIView(APIView):
	permission_classes = [permissions.IsAuthenticated,]
	def post(self, request):
		if(request.user.is_authenticated):
			data = request.data
			data['AddedBy']=request.user.id
			serializer = serializers.QuestionSerializer(data=data)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(serializer.data, status=201)
		else:
			data = [{'status': 'unauthorized'}]
			return Response(data, status=201)


class UserAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.UserSerializer()
    def get(self, request):
    	queryset = models.CustomUser.objects.filter(id =request.user.id).values()
    	data = {'currentuser': queryset[0]}
    	return Response(data,status=200,content_type="application/json")

class GETQuestions(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = models.Questions.objects.all()
    serializer_class = serializers.QuestionSerializer


class CreateQuiz(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
    	if(request.user.is_authenticated):
    		data = request.data
    		quizdata = data['quiz']
    		quizdata['AddedBy'] = request.user.id
    		serializer = serializers.QuizSerializer(data=quizdata)
    		serializer.is_valid(raise_exception=True)
    		serializer.save()
    		return Response(serializer.data, status=201)

class CreateQuizQuestions(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
    	if(request.user.is_authenticated):
    		data = request.data
    		print("hewewe")
    		quizid = data['quizid']
    		quizquestions=request.data.get('quizquestions',[])
    		for ques in quizquestions:
    			quesdata = {'quiz': quizid,'question':ques}
    			serializer = serializers.QuizquestionSerializer(data=quesdata)
    			serializer.is_valid(raise_exception=True)
    			serializer.save()	
    		return Response({'status': 'Successfully Created'}, status=201)

# def QuizListApi(gene)


