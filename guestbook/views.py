from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
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
        Record.objects.create(**form.cleaned_data)
        return redirect('index')


def update_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record.name = form.clean_name()
            record.email = form.cleaned_data['email']
            record.text = form.clean_text()
            record.status = form.cleaned_data['status']
            record.save()
            return redirect('index')
    else:
        form = RecordForm(initial={
            'name': record.name,
            'email': record.email,
            'text': record.text,
            'status': record.status
        })
    return render(request, 'record_update.html', {'form': form, 'record': record})


def delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('index')
    context = {
        'record': record,
    }
    return render(request, 'record_delete.html', context)
