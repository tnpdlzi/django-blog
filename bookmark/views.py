from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView) :
    model = Bookmark

class BookmakrDV(DetailView) :
    model = Bookmark
