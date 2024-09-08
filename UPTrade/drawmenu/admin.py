from django.contrib import admin
from .models import MenuItem, Menu


from .models import Menu, MenuItem

admin.site.register(Menu)
admin.site.register(MenuItem)

# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description']
#
# @admin.register(MenuItem)
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ['cat', 'parent', 'url']