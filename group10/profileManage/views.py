from django.shortcuts import render
import pyrebase
# Create your views here.

config = {
  "apiKey": "AIzaSyDY6UV8OBpaUuKdsUPdtvNwUxfZKPl4nMw",
  "authDomain": "profile-management-473b0.firebaseapp.com",
  "databaseURL": "https://profile-management-473b0-default-rtdb.firebaseio.com",
  "projectId": "profile-management-473b0",
  "storageBucket": "profile-management-473b0.appspot.com",
  "messagingSenderId": "64112140710",
  "appId": "1:64112140710:web:9ca806a20c3f34fc0aaf67",
  "measurementId": "G-JRMV1QMYTR"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def index(request):
    #accessing our firebase data and storing it in a variable
    email = database.child('data').child('email').get().val()
    phone = database.child('data').child('phone').get().val()
    userName = database.child('data').child('username').get().val()


    context = {
        'email':email,
        'phone':phone,
        'userName':userName
    }

    return render(request, 'index.html', context)