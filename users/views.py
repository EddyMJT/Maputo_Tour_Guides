from django.shortcuts import render, HttpResponseRedirect, reverse, Http404
from django.contrib.auth import logout

def users(request):
    return render(request, "users/change_user_settings.html", {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('tours:home'))


def custom_login(request):
    return render(request, 'users/login.html', {})


def register(request):
    return render(request, 'users/register.html', {})


def check_is_superuser(request):
    if not request.user.is_superuser:
        raise Http404


def user_settings(request):
    return render(request, 'users/user_settings.html', {})


def edit_settings(request, user_id):
    return render(request, 'users/change_user_settings.html', {})
