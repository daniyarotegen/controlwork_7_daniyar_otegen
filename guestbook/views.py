from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from guestbook.forms import RecordForm
from guestbook.models import Record, StatusChoice


def index_view(request: WSGIRequest):
    records = Record.objects.exclude(status=StatusChoice.BLOCKED).order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'index.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'record_create.html', {'form': form})
    form = RecordForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'record_create.html', context={
            'form': form
        })
    else:
        record = Record.objects.create(**form.cleaned_data)
        return redirect('index')
