from django.contrib import admin

from .models import Produto, Codigo

#class UserAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        if request.user.is_superuser:
#            obj.is_staff = True
#            obj.save()

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Produto, ProdutoAdmin)
#admin.site.register(UserAdmin)
admin.site.register(Codigo)
