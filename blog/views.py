from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from django.contrib.auth.decorators import login_required
from .forms import TopicForm

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
    return render(request, 'blog/topic_entry.html', {})


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

