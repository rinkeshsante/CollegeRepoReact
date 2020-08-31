from django.contrib import admin

from.models import Lab, Department, Equipment, Software, ComputerSoftwareMapping, Computer

# class EquipmentInline(admin.TabularInline):
#     model =Equipment
#     list_display=('code','name',)


class LabAdmin(admin.ModelAdmin):

    list_display = ('code', 'name', 'lab_number',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gi_no', 'code', 'lab')


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gi_no', 'code', 'lab')


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'gi_no', 'code')

# class LabFacultyMappingAdmin(admin.ModelAdmin):
#     list_display=('lab','faculty')


admin.site.register(Department)
admin.site.register(Lab, LabAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerSoftwareMapping)

# admin.site.register(LabEquipmentMapping)
# admin.site.register(LabFacultyMapping, LabFacultyMappingAdmin)
