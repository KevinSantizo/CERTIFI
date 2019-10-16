from django.contrib import admin
from sport.models import Reservation,  Field, Company


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('company_reserve', 'customer_reserve', 'field_reserve', 'schedule_date', 'schedule_time')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'image')


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'type', 'price')