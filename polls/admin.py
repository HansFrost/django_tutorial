from django.contrib import admin
from .models import Question

# from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
# admin.site.register(Question)


@admin.register(Question)
class ViewAdmin(ImportExportActionModelAdmin):
    pass


# @admin.register(Question)
# class QuestionResource(resources.ModelResource):
#    class Meta:
#        model = Question
#        fields = ("id", "question_text", "pub_date")

