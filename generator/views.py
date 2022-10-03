from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import random

# funcion about
def about(request):
    return render(request,'about.html')


def home(request):
    return render(request, 'home.html' )


def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')

    generated_password = ''

    length = int(request.GET.get('length'))

    # para letras mayusculas
    if request.GET.get('uppercase'):

        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    # para caracteres especiales
    if request.GET.get('special'):

        characters.extend(list('°!#$%&/()=?¡¿+{-\*][}.,;:_'))
        
    if request.GET.get('numbers'):

        characters.extend(list('1234567890'))
        

    for x in range(length):

        generated_password += random.choice(characters)


    return render(request, 'password.html', {
        'password': generated_password
    })