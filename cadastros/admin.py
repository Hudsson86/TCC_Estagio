from django.contrib import admin
from django.contrib.auth.models import update_last_login
from .models import Vaga


@admin.register(Vaga)

class VagaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
