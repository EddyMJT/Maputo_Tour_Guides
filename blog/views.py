from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm

def blog(request):
    """Main page of blog. Shows all blog posts"""

    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'blog/blog.html', context)


def topic(request, topic_id, topic_title):
    """Renders all posts of a given topic"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context)



def topic_entry(request, topic_id, entry_id, entry_title):
    """Renders the text and image for individual post"""
    topics = Topic.objects.all()
    entries = Entry.objects.all()

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    context = {'topic': topic, 'entry': entry, 'topics': topics, 'entries': entries}

    return render(request, 'blog/topic_entry.html', context)


@login_required()
def new_topic(request):
    """Allows User to Enter New Topic"""

    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

        return HttpResponseRedirect(reverse("blog:blog"))
    context = {"form": form}
    return render(request, 'blog/new_topic.html', context)



@login_required()
def edit_topic(request, topic_id):
    """Allows User to edit the Topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user and not request.user.is_superuser:
        raise Http404

    if request.method != "POST":
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("blog:blog"))
    context = {"form": form, "topic": topic}

    return render(request, "blog/edit_topic.html", context)


@login_required()
def new_topic_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user and not request.user.is_superuser:
        raise Http404

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic_entry = form.save(commit=False)
            new_topic_entry.topic = topic
            new_topic_entry.save()
        return HttpResponseRedirect(reverse("blog:topic", args=[topic_id, topic.slug_title]))
    context = {"form": form, "topic": topic}

    return render(request, "blog/new_topic_entry.html", context)


@login_required()
def edit_topic_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user and not request.user.is_superuser:
        raise Http404

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("blog:topic_entry", args=[topic.id, entry_id, topic.slug_title]))
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "blog/edit_topic_entry.html", context)


@login_required()
def delete_topic(request, topic_id):
    """deletes the desired topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    if topic.owner != request.user and not request.user.is_superuser:
        raise Http404
    return HttpResponseRedirect(reverse("blog:blog"))



@login_required()
def delete_topic_entry(request, entry_id):
    """deletes the desired entry and returns to topic."""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user and not request.user.is_superuser:
        raise Http404
    Entry.objects.filter(id=entry_id).delete()
    return HttpResponseRedirect(reverse("blog:topic", args=[topic.id]))

