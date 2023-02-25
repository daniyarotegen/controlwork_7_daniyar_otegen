from django.contrib import admin
from guestbook.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'created_at', 'updated_at', 'status')
    list_filter = ('name', 'email', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'status')
    fields = ('name', 'email', 'text', 'created_at', 'updated_at', 'status')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Record, RecordAdmin)
