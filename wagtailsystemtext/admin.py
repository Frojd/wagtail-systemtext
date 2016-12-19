from django.contrib import admin

from wagtailsystemtext.models import SystemString


class SystemStringAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'string', 'group', 'site')

    class Meta:
        model = SystemString

admin.site.register(SystemString, SystemStringAdmin)
