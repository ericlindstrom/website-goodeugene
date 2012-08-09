from django.contrib import admin
from models import *

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


class AbstractPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'order', 'visible')
    list_editable = ('visible', 'order')
    save_on_top = True

 
class RoleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('project_admin_title', 'client', 'category', 'order', 'visible',)
    list_editable = ('visible', 'order')
    save_on_top = True
    inlines = [ImageInline,]


admin.site.register(Client, AbstractPortfolioAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Credit, admin.ModelAdmin)
admin.site.register(Category, AbstractPortfolioAdmin)
#admin.site.register(Tag, AbstractPortfolioAdmin)
