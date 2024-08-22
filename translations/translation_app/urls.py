from django.urls import path
from . import views

app_name = 'translation_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:entry_id>/', views.entry, name='entry'),
    path('sport/<str:topic_name>/', views.topic, name='topic'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
