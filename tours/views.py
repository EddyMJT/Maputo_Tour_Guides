from django.shortcuts import render



def home(request):


    return render(request, 'tours/home.html', {})


def about_us(request):
    pass