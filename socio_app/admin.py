from django.contrib import admin
from .models import AddService,Queries,Answers

# Register your models here.
class ApprovalAdmin(admin.ModelAdmin):
    list_filter = ('approval',)

admin.site.register(Queries,ApprovalAdmin)
admin.site.register(AddService)
admin.site.register(Answers)
