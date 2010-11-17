from django.contrib import admin
from thefoundation.funding.models import Contribution, Grant

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('year','contributor','amount')
    list_filter = ('year',)
    search_fields = ('contributor','note')
admin.site.register(Contribution, ContributionAdmin)

class GrantAdmin(admin.ModelAdmin):
    list_display = ('year','recipient','amount')
    list_filter = ('year','is_minigrant')
    search_fields = ('recipient','purpose')
admin.site.register(Grant, GrantAdmin)