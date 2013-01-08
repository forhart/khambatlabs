from django.contrib import admin
from khambatlabs.models import Patient,Sample,Test,Hospital,Doctor

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gender','age')
    search_fields = ('first_name', 'last_name')
    

class SampleAdmin(admin.ModelAdmin):
    list_display = ('patient','doctor','hospital','count_tests','list_tests','Taken')
    list_filter = ('Taken','test','doctor','hospital')
    fieldsets = [
        ("Time & Date", {'fields': ['Taken']}),
        ('Patient Information', {'fields': ['patient']}),
        ('Doctor Information', {'fields': ['doctor']}),
        ('Hospital Information', {'fields': ['hospital']}),
        ('Select Tests', {'fields': ['test']}),
    ]


class TestAdmin(admin.ModelAdmin):
    list_display = ('name','price')

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoctorAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","gender","age")





admin.site.register(Patient,PatientAdmin)
admin.site.register(Sample,SampleAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Doctor,DoctorAdmin)
