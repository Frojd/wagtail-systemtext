from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from wagtailsystemtext.utils import get_admin_site
from wagtailsystemtext.models import SystemString


class SystemStringAdmin(ModelAdmin):
    model = SystemString
    menu_label = 'System Text'
    menu_order = 200
    list_display = ('identifier', 'string', 'group', 'site')
    search_fields = ('identifier', 'string')
    add_to_settings_menu = True

    def get_queryset(self, request):
        qs = super(SystemStringAdmin, self).get_queryset(request)
        return qs.filter(site=get_admin_site())

modeladmin_register(SystemStringAdmin)
