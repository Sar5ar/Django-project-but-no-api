from django.contrib import admin
from .models import ser,Tavarlar,saqlash
from .form import userform,userformch
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class Adm(UserAdmin):
    add_form=userform
    form=userformch
    model=ser
    list_display=['username','first_name','last_name','email','manzil','is_staff','rasmingiz']
    fieldsets=UserAdmin.fieldsets + (
        (None,{"fields":("manzil",'rasmingiz')}),
    )
    add_fieldsets=UserAdmin.add_fieldsets + (
        (None,{"fields":("manzil",'rasmingiz')}),
    )
class adm(admin.ModelAdmin):
    list_display =['nomi','rasmi','narxi']

admin.site.register(saqlash)
admin.site.register(Tavarlar,adm)

admin.site.register(ser,Adm)