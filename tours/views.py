from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .forms import TourForm, ReviewForm
from .models import Tour, Photo, Review
import random
from django.utils.text import slugify


def check_is_superuser(request):
    if not request.user.is_superuser:
        raise Http404


def home(request):
    tours = Tour.objects.all()
    """Creating three lists with different tours and a review list to display on the home page """
    fd_tours_list = home_fd_tours(tours)
    walking_tours_list = home_walking_tours(tours)
    on_wheels_tours_list = home_wheels_tours(tours)
    reviews_list = home_reviews()  # Get three random reviews to display on the home page

    context = {'tours': tours, 'reviews_list': reviews_list, 'fd_tours_list': fd_tours_list,
               'walking_tours_list': walking_tours_list, 'on_wheels_tours_list': on_wheels_tours_list}
    return render(request, 'tours/home.html', context)


def about_us(request):
    return render(request, "tours/about_us.html", {})


def remove_guide(request, guide_id):
    return HttpResponseRedirect(reverse("tours:about_us"))


def edit_guide_info(request, guide_id):
    return render(request, "tours/edit_guide_info.html", {})


def add_guide(request):
    return render(request, "tours/add_guide.html", {})


def guide_bio(request, guide_id):
    return render(request, "tours/guide_bio.html", {})


@login_required
def new_tour(request):

    check_is_superuser(request)
    if request.method != "POST":
        form = TourForm()
    else:
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("tours:our_tours"))
    context = {"form": form}
    return render(request, "tours/new_tour.html", context)


@login_required
def edit_tour(request, tour_id):

    check_is_superuser(request)
    tour = Tour.objects.get(id=tour_id)
    if request.method != "POST":
        form = TourForm(instance=tour)
    else:
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("tours:tour_info", args=[tour_id, tour.slug_title]))
    context = {"tour": tour, "form": form}
    return render(request, "tours/edit_tour.html", context)


def home_reviews():
    """Generates a List with Three Random Reviews to display on the home page."""

    reviews = Review.objects.all()
    review_list = []
    if len(reviews) > 3:
        "If there are more than three review, pick any three"
        review = reviews[random.randint(0, len(reviews) - 1)]
        review_list = [review]
        counter = 1
        while counter < 3:
            review = reviews[random.randint(0, len(reviews) - 1)]
            review_counter = 0
            for index in range(len(review_list) - 1):
                if review == review_list[index]:
                    review_counter += 1
            if review_counter < 1:
                review_list.append(review)
                counter += 1
    elif len(reviews) > 0:
        "If there are less than 3 reviews, use all available reviews"
        for review in reviews:
            review_list.append(review)
    else:
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


def our_tours(tour_category):
    tours = Tour.objects.all()
    safari_tour_list = []
    subcategory_list = []
    for tour in tours:
        """Creates a List of Tours that are of the same category"""
        if tour.category == tour_category:
            safari_tour_list.append(tour)
            subcategory_list.append(tour.subcategory)
    if len(subcategory_list) >= 1:
        final_subcategory_list = [subcategory_list[0]]
    else:

        final_subcategory_list = ["No {} Added  Yet".format(tour_category)]

    for category in subcategory_list:
        counter = 0
        for i in range(len(final_subcategory_list)):
            if category == final_subcategory_list[i]:
                counter += 1
        if counter < 1:
            final_subcategory_list.append(category)

    context = {"safari_tour_list": safari_tour_list, "subcategory_list": final_subcategory_list, "tours": tours,
               "category": tour_category}
    return context


def safari(request):
    """Renders The Safari page"""
    category = "Safaris"
    context = our_tours(category)
    return render(request, 'tours/our_tours.html', context)


def beach_tours(request):
    category = "Beach Tours"
    context = our_tours(category)
    return render(request, 'tours/our_tours.html', context)


def city_tours(request):
    category = "City Tours"
    context = our_tours(category)
    return render(request, 'tours/our_tours.html', context)


def cultural_tours(request):
    category = "Cultural Tours"
    context = our_tours(category)
    return render(request, 'tours/our_tours.html', context)


def transfers(request):
    category = "Transfers"
    context = our_tours(category)
    return render(request, 'tours/our_tours.html', context)


def add_photos(request, tour_title, tour_id):
    return render(request, "tours/add_photos.html", {})


def delete_photo(request, photo_id):
    return HttpResponseRedirect(reverse("tours:tour_photos"))


def photo(request, photo_id):
    return render(request, "tours/photo.html", {})


def tour_photos(request, tour_id, tour_title):
    """Renders and displays the page with photos of a specific tour."""

    tour = Tour.objects.get(id=tour_id)
    photos = Photo.objects.all()

    context = {"tour": tour, "photos": photos}
    return render(request, "tours/tour_photos.html", context)


def tour_info(request, tour_id, tour_title):

    tour = Tour.objects.get(id=tour_id)
    tour_title = slugify(tour.title)
    tours = Tour.objects.all()
    similar_tours_list = []
    not_similar_tours_list = []
    other_tour = tour.category
    size_flag = False
    # Choose a random list of Other tours
    while other_tour == tour.category and size_flag == False:
        if len(tours) >= 2:
            index = random.randint(1, len(tours) - 1)
            more_tour = tours[index]
            if more_tour.category != tour.category:
                other_tour = more_tour.category
        else:
            size_flag = True

    for tours_element in tours:
        if tours_element.category == tour.category:
            similar_tours_list.append(tours_element)
        elif tours_element.category == other_tour:
            not_similar_tours_list.append(tours_element)

    context = {"tour": tour, "similar_tours_list": similar_tours_list, "not_similar_tours_list": not_similar_tours_list,
               "tour_title": tour_title}
    return render(request, "tours/tour_info.html", context)


def delete_tour(request, tour_id):

    check_is_superuser(request)
    tour = Tour.objects.get(id=tour_id)
    tour.delete()
    return HttpResponseRedirect(reverse("tours:our_tours"))


def gallery(request):
    return render(request, 'tours/gallery.html', {})


def reviews(request):
    """Renders and displays reviews..."""

    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'tours/reviews.html', context)



@login_required()
def delete_review(request, review_id):
    """Deletes an individual review of a tour."""

    check_is_superuser(request)
    review = Review.objects.get(id=review_id)
    review.delete()
    return HttpResponseRedirect(reverse("tours:reviews"))


@login_required()
def new_review(request, tour_id, tour_title):

    check_is_superuser(request)
    tour = Tour.objects.get(id=tour_id)
    if request.method != "POST":
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.tour = tour
            new_review.save()
            return HttpResponseRedirect(reverse("tours:reviews"))

    context = {"form": form, 'tour': tour}
    return render(request, "tours/new_review.html", context)



def success(request):
    return render(request, 'tours/success.html')


def contacts(request):
    return render(request, 'tours/contacts.html')

