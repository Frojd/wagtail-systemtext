from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from wagtailsystemtext.models import SystemString


class SystemStringAdmin(ModelAdmin):
    model = SystemString
    menu_label = 'Translations'
    menu_order = 200
    list_display = ('identifier', 'string', 'site', 'group')
    search_fields = ('identifier', 'string')
    add_to_settings_menu = True

modeladmin_register(SystemStringAdmin)
