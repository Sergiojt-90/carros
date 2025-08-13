from django.contrib import admin
from cars.models import Car, Brand #, Model_Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id','model', 'brand', 'factory_year','model_year','value', 'photo')
    search_fields = ('model','brand')
   

class BrandAdmin(admin.ModelAdmin):
   list_display = ('name',) 
   search_fields = ('name',)

'''class Model_CarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)'''


admin.site.register(Car, CarAdmin)
admin.site.register(Brand,BrandAdmin)
#admin.site.register(Model_Car, Model_CarAdmin)
