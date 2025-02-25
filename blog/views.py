from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def blog(request):
    return render(request, 'blog/blog.html', {})


def topic(request, topic_id, topic_title):
    return render(request, 'blog/topic.html', {})


def topic_entry(request, topic_id, entry_id, entry_title):
    return render(request, 'blog/topic_entry.html', {})


def new_topic(request):
    return render(request, 'blog/new_topic.html', {})


def edit_topic(request, topic_id):
    return render(request, "blog/edit_topic.html", {})


def new_topic_entry(request, topic_id):
    return render(request, "blog/new_topic_entry.html", {})


def edit_topic_entry(request, entry_id):
    return render(request, "blog/edit_topic_entry.html", {})


def delete_topic(request, topic_id):
    return HttpResponseRedirect(reverse("blog:blog"))


def delete_topic_entry(request, entry_id):
    return HttpResponseRedirect(reverse("blog:blog"))

