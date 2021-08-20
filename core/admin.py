from django.contrib import admin

# Register your models here.

from .models import company

@admin.register(company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cnpj','nome_fantasia','data_abertura','active','id_usuario')
