from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404


def home(request):
    return render(request, "tours/home.html", {})


def about_us(request):
    return render(request, "tours/about_us.html", {})


def check_is_superuser(request):
    if not request.user.is_superuser:
        raise Http404


def remove_guide(request, guide_id):
    return HttpResponseRedirect(reverse("tours:about_us"))


def edit_guide_info(request, guide_id):
    return render(request, "tours/edit_guide_info.html", {})


def add_guide(request):
    return render(request, "tours/add_guide.html", {})


def guide_bio(request, guide_id):
    return render(request, "tours/guide_bio.html", {})


def new_tour(request):
    return render(request, "tours/new_tour.html", {})


def edit_tour(request, tour_id):
    return render(request, "tours/edit_tour.html", {})


def home_reviews():
    review_list = ["No reviews available yet!"]
    return review_list


def home_fd_tours(tours):
    """Creates a list with a few day tour activities"""
    full_day_tours_list = []
    for tour in tours:
        if tour.home_page == "Yes" and tour.category == "Safaris":
            full_day_tours_list.append(tour)
        elif tour.home_page == "Yes" and tour.category =="Beach Tours":
            full_day_tours_list.append(tour)
        elif tour.home_page == "Yes" and tour.subcategory == "eSwatini Full day Tour":
            full_day_tours_list.append(tour)
        elif tour.home_page == "Yes" and tour.subcategory == "Other Tours":
            full_day_tours_list.append(tour)
        elif tour.home_page == "Yes" and tour.subcategory == "Cultural Tours":
            full_day_tours_list.append(tour)

    return full_day_tours_list


def home_walking_tours(tours):
    """Create a list with a few walking tour activities"""
    walking_tours_list = []
    for tour in tours:
        if tour.subcategory == "Walking Tours" and tour.home_page == "Yes":
            walking_tours_list.append(tour)

    return walking_tours_list


def home_wheels_tours(tours):
    """Create a list with a few on wheels tour activities"""
    on_wheels_tours_list = []
    for tour in tours:
        if tour.subcategory == "On wheels Tours" and tour.home_page == "Yes":
            on_wheels_tours_list.append(tour)

    return on_wheels_tours_list


def our_tours(request):
    return render(request, "tours/our_tours.html", {})


def safari(request):
    return render(request, 'tours/our_tours.html', {})


def beach_tours(request):
    return render(request, 'tours/our_tours.html', {})


def city_tours(request):
    return render(request, 'tours/our_tours.html', {})


def cultural_tours(request):
    return render(request, 'tours/our_tours.html', {})


def transfers(request):
    return render(request, 'tours/our_tours.html', {})


def add_photos(request, tour_title, tour_id):
    return render(request, "tours/add_photos.html", {})


def delete_photo(request, photo_id):
    return HttpResponseRedirect(reverse("tours:tour_photos"))


def photo(request, photo_id):
    return render(request, "tours/photo.html", {})


def tour_photos(request, tour_id, tour_title):
    return render(request, "tours/tour_photos.html", {})


def tour_info(request, tour_id, tour_title):
    return render(request, "tours/tour_info.html", {})


def delete_tour(request, tour_id):
    return HttpResponseRedirect(reverse("tours:our_tours"))


def gallery(request):
    return render(request, 'tours/gallery.html', {})


def reviews(request):
    return render(request, 'tours/reviews.html', {})


def delete_review(request, review_id):
    return HttpResponseRedirect(reverse("tours:reviews"))


def new_review(request, tour_id, tour_title):
    return render(request, "tours/new_review.html", {})


def success(request):
    return render(request, 'tours/success.html')


def contacts(request):
    return render(request, 'tours/contacts.html')

