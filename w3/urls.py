"""Defines URL patterns for app w3."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$',
        views.index,
        name='index'),

    # Contact information
    url(r'^contact$',
        views.contact,
        name='contact'),

    # Pls Hire me!
    url(r'^employer$',
        views.employer,
        name='employer'),

    # Install Instructions
    url(r'^install_Ins$',
      views.install_Ins,
      name='install_ins'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$',
        views.topic,
        name='topic'),

    # Show all topics
    url(r'^topics/$',
        views.topics,
        name='topics'),

    # Page for adding a new topic
    url(r'^new_topic/$',
        views.new_topic,
        name='new_topic'),

    # page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$',
        views.new_entry,
        name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$',
        views.edit_entry,
        name='edit_entry'),
]