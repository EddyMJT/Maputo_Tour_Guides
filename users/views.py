from django.shortcuts import render


def users(request):

    return render(request, "users/change_user_settings.html", {})

