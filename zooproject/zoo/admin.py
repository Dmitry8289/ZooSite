from django.contrib import admin

from zoo.models import Zoo


@admin.register(Zoo)
class ZooAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_added', )
    list_display = ('name', 'animal_type', 'date_of_added')
    search_fields = ('name', 'animal_type')
    list_filter = ('date_of_added', )