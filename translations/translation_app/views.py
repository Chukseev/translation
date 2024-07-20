from django.shortcuts import render
from .models import Topic, Entry


def index(request):
    entries = Entry.objects.order_by('-date_added')
    topics = Topic.objects.order_by('date_added')
    context = {'entries': entries, 'topics': topics}
    return render(request, 'translation_app/index.html', context)


def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'translation_app/entry.html', context)


def topic(request, topic_id):
    entries_in_topic = Entry.objects.filter(topic=topic_id)
    print(entries_in_topic)
    topic = Topic.objects.get(id=topic_id)
    print(topic)
    context = {'entries_in_topic': entries_in_topic, 'topic': topic}
    return render(request, 'translation_app/entry_in_topic.html', context)
