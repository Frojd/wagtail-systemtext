from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from wagtail.contrib.modeladmin.views import EditView, CreateView

from wagtailsystemtext import app_settings
from wagtailsystemtext.utils import get_admin_site, fill_cache
from wagtailsystemtext.models import SystemString


class SystemStringEditView(EditView):
    def form_valid(self, form):
        redirect = super(SystemStringEditView, self).form_valid(form)
        self.instance.modified = True
        self.instance.save()

        if app_settings.SYSTEMTEXT_REBUILD_ON_SAVE:
            fill_cache(get_admin_site())
        return redirect


class SystemStringCreateView(CreateView):
    def form_valid(self, form):
        redirect = super(SystemStringCreateView, self).form_valid(form)
        if app_settings.SYSTEMTEXT_REBUILD_ON_SAVE:
            fill_cache(get_admin_site())
        return redirect


class SystemStringAdmin(ModelAdmin):
    model = SystemString
    menu_label = 'System Text'
    menu_order = 200
    list_display = ('modified', 'identifier', 'string', 'group', 'site')
    search_fields = ('identifier', 'string')
    add_to_settings_menu = True
    create_view_class = SystemStringCreateView
    edit_view_class = SystemStringEditView

    def get_queryset(self, request):
        qs = super(SystemStringAdmin, self).get_queryset(request)

        site = get_admin_site()
        if site:
            qs = qs.filter(site=site)

        return qs


modeladmin_register(SystemStringAdmin)
