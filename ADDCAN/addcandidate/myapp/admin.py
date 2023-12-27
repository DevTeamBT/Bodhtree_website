from django.contrib import admin
from myapp.models import Add_requirement
# class AddreqAdmin(admin.ModelAdmin):
#     list_display=('client','contact','title_for_req','priority','skillsets','must_have','good_to_have','exp_range_min','max','budget_min','budget_max','positions','location','hire_type','work_type','recruiter','account_mgr')


# Register your models here.
admin.site.register(Add_requirement)