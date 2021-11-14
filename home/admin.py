from django.contrib import admin
from home.models import Institute

# Register your models here.
@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display=['institute_name','institute_owner','institute_status','institute_created_date','institute_expiry_date','institute_remarks']