from django.contrib import admin


from .models import Unit, Reach


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('first_name',)


@admin.register(Reach)
class ReachAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
