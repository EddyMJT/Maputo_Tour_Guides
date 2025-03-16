from django.shortcuts import render, HttpResponseRedirect, reverse, Http404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def users(request):
    return render(request, "users/change_user_settings.html", {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('tours:home'))



def custom_login(request):
    form = AuthenticationForm(data=request.POST or None)  # Create form instance
    if request.method == 'POST':
        if form.is_valid():
            # Authenticate the user
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                try:
                    # Check if the user has a profile and if they are approved
                    if user.profile.is_approved:  # Ensure user has profile and approval
                        login(request, user)
                        return HttpResponseRedirect(reverse('tours:home'))
                    else:
                        messages.error(request, "Your account is pending approval.")
                except user.profile.DoesNotExist:
                    messages.error(request, "User account does not exist. Please contact support.")
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html', {'form': form})


def register(request):

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            return HttpResponseRedirect(reverse('tours:home'))
    context = {'form': form}
    return render(request, 'users/register.html', context)


def check_is_superuser(request):
    if not request.user.is_superuser:
        raise Http404


@login_required()
def user_settings(request):
    """Approves New Users"""
    profiles = Profile.objects.all()
    check_is_superuser(request)
    return render(request, 'users/user_settings.html', {'profiles': profiles})


@login_required()
def edit_settings(request, user_id):
    check_is_superuser(request)
    user = Profile.objects.get(id=user_id)
    if request.method != 'POST':
        form = UserForm(instance=user)
        print(user)
    else:
        form = UserForm(request.POST, instance=user)
        print(user, user.is_approved)
        if form.is_valid():
            form.save()
            print("Save")
        return HttpResponseRedirect(reverse('users:user_settings'))

    context = {'form': form, 'user': user, }
    return render(request, 'users/change_user_settings.html', context)