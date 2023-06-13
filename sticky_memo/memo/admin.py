from django.contrib import admin
from memo.models import Memo

# Register your models here.
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title']