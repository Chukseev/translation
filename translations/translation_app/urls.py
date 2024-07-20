from django.urls import path
from . import views

app_name = 'translation_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:entry_id>/', views.entry, name='entry'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]
