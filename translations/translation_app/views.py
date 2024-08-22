from django.shortcuts import render, redirect
from .models import Topic, Entry


def index(request):
    entries = Entry.objects.order_by('-date_added')
    topics = Topic.objects.order_by('date_added')
    context = {'entries': entries, 'topics': topics}
    return render(request, 'translation_app/index.html', context)


def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topics = Topic.objects.order_by('date_added')
    context = {'entry': entry, 'topics': topics}
    return render(request, 'translation_app/entry.html', context)


def topic(request, topic_name):
    topic = Topic.objects.get(text=topic_name)
    entries_in_topic = Entry.objects.filter(topic=topic.id)
    topics = Topic.objects.order_by('date_added')
    context = {'entries_in_topic': entries_in_topic, 'topic': topic, 'topics': topics}
    return render(request, 'translation_app/entry_in_topic.html', context)


def privacy(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'translation_app/privacy.html', context)


def terms(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'translation_app/terms.html', context)
