from django.shortcuts import render



def home(request):

    context = {}
    return render(request, "tours/home.html", context)


def about_us(request):

    context = {}

    return render(request, "tours/about_us.html", context)
