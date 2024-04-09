from django.contrib import admin
from .models import Order , OrderItem

class ReadOnlyModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        # if request.method not in ('GET', 'HEAD'):
        #     return False
        # return super().has_change_permission(request, obj)
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'status', 'created_at','total_price']
    readonly_fields = ['user', 'created_at','total_price']

    def has_change_permission(self, request, obj=None):
        if obj and obj.status != 'pending':
            return False
        return super().has_change_permission(request, obj)


# Register your models here.
admin.site.register(OrderItem, ReadOnlyModelAdmin)
admin.site.register(Order, OrderAdmin)
