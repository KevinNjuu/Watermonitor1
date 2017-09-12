# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Network, Primary_canal, Secondary_canal, Tertiary_canal

class Primary_canalInline(admin.TabularInline):
    model = Primary_canal
    extra = 1

class Secondary_canalInline(admin.TabularInline):
    model = Secondary_canal
    extra = 1

class Tertiary_canalInline(admin.TabularInline):
    model = Tertiary_canal
    extra = 1

class NetworkAdmin(admin.ModelAdmin):

    list_display = ('network_name', 'network_code', 'physical_address', 'contact_person', 'mobile')
    list_filter = ['network_name']
    search_fields = ['network_name']

    fieldsets = [
        ('Network Information', {'fields':['network_name', 'network_code']}),
        ('Contact Information', {'fields': ['physical_address','contact_person', 'mobile']}),
    ]

    inlines = [Primary_canalInline]

'''class Primary_CanalAdmin(admin.ModelAdmin):
    inlines = [Secondary_canalInline]'''



admin.site.register(Network, NetworkAdmin)
admin.site.register(Primary_canal)
admin.site.register(Secondary_canal)
admin.site.register(Tertiary_canal)


