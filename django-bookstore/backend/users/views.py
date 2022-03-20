from django.shortcuts import render, redirect, HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

#from django.contrib.auth.forms import UserCreationForm
#from .forms import UserRegisterForm
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required


#def home(request):
 #   return render(request, 'users/home.html')


#def register(request):
   # if request.method == "POST":
   #     form = UserRegisterForm(request.POST)
   #     if form.is_valid():
   #         form.save()
   #         username = form.cleaned_data.get('username')
   #         messages.success(request, f'Hi {username}, your account was created successfully')
   #         return redirect('home')
    #else:
    #    form = UserRegisterForm()

    #return render(request, 'users/register.html', {'form': form})


#@login_required()
#def profile(request):
    #return render(request, 'users/profile.html')


#register API
#class RegisterAPI(generics.GenericAPIView):
#    serializer_class = UserSerializer
    
#    def post(self, request, *args, **kwargs):
#        serializer = self.get_serializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        user = serializer.save()
#        return Response({
#        "user": UserSerializer(user, context=self.get_serializer_context()).data,
#        "token": AuthToken.objects.create(user)[1]
#        })


#accounts API
#class LoginAPI(KnoxLoginView):
#    permission_classes = (permissions.AllowAny,)
    
#    def post(self, request, format=None):
#        serializer =AuthTokenSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        user = serializer.validated_data['user']
#        login(request, user)
#        return super(LoginAPI,self).post(request, format=None)


@csrf_exempt
def List_All_Users(request):
    users = Users.objects.all()

    if request.method == 'GET':
        serializer = UserSerializer(users, many = True)
        return JsonResponse(serializer.data, status = 200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

