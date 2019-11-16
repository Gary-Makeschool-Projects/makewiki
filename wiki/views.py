from django.shortcuts import render, get_object_or_404
from wiki.models import Page

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    template_name = 'wiki/list.html'


class PageDetailView(DetailView):
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug."""
        page = get_object_or_404(Page, slug=slug)
        return render(request, 'wiki/page.html', context={'page': page})

    def post(self, request, slug):
        pass
