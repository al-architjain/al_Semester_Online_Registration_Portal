from django.contrib import admin
from . import models
# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_name']
    ordering = ['id']

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_name')
    ordering = ['id']

class ResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll_no', 'semester', 'sgpi', 'cgpi']
    ordering = ['roll_no', 'semester']

class UGBranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'code' , 'name', 'full_name']
    ordering = ['id']


admin.site.register(models.Board, TitleAdmin)
admin.site.register(models.Category, TitleAdmin)
admin.site.register(models.UGClass, TitleAdmin)
admin.site.register(models.UGBranch, UGBranchAdmin)
admin.site.register(models.Subjects)
admin.site.register(models.Documents, DocumentsAdmin)
admin.site.register(models.Result, ResultsAdmin)
admin.site.register(models.DocumentInfo)
admin.site.register(models.StudentInfo)
admin.site.register(models.StudentFirstFeeStatus)
admin.site.register(models.Due)


# admin.site.register(models.)