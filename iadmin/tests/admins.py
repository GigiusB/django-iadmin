from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from iadmin.actions import mass_update
from iadmin.api import *
from iadmin.filters import RelatedFieldComboFilter, RelatedFieldCheckBoxFilter, RelatedFieldRadioFilter

class IUserAdmin(UserAdmin, IModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', '_groups', 'last_login')
    list_display_links = ('username', 'first_name', 'last_name')

    cell_filter = ('email', 'is_staff', 'last_name', 'last_login')
    cell_filter_operators = {'last_login': ('exact', 'not', 'lt', 'gt')}


    list_filter = ( ('groups',RelatedFieldCheckBoxFilter), )
    search_fields = ('username', )
    actions = [mass_update]

    def _groups(self, obj):
        return ",".join( [o.name for o in obj.groups.all()])
    _groups.short_description = 'Groups'


class IUserInline(ITabularInline):
#    model = User
    model = User.groups.through
#    readonly_fields = ('user', )
    extra = 0

class IGroupAdmin(GroupAdmin, IModelAdmin):
    inlines = (IUserInline, )

class IContentType(IModelAdmin):
    list_display = ('name', 'app_label', 'model', )

class IPermission(IModelAdmin):
    list_display = ('name', 'content_type', 'codename', )
    search_fields = ('name'),
    list_filter = cell_filter = ('content_type', )

force_register(User, IUserAdmin, adminsite=isite)
force_register(Group, IGroupAdmin, adminsite=isite)
force_register(Permission, IPermission, adminsite=isite)
force_register(ContentType, IContentType, adminsite=isite)