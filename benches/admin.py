from django.contrib import admin
from .models import BenchType, BenchDistrict, Bench

@admin.register(BenchType)
class BenchTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'avatar')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BenchDistrict)
class BenchDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'avatar')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Bench)
class BenchAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'type', 'district')
    search_fields = ('name', 'created_date')
    list_filter = ('type', 'district')
