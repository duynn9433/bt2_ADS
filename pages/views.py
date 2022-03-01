from django.shortcuts import render

# Create your views here.
from pages.models import Pages


def index(request, pagename):
    pagename = '/' + pagename
    pg = Pages.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }

    return render(request, 'pages/page.html', context)
