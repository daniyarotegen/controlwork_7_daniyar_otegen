from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from guestbook.models import Record, StatusChoice


def index_view(request: WSGIRequest):
    records = Record.objects.exclude(status=StatusChoice.BLOCKED).order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'index.html', context=context)
