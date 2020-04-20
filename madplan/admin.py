from django.contrib import admin
from .models import (
    IngredientCategory,
    Course,
    Measurement,
    Blogger,
    Macronutrient,
    Recipe,
    Ingredient,
    Quantity,
    RecipeStep,
    RecipeDescription,
)
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
@admin.register(
    Recipe, RecipeDescription, Ingredient, Measurement, Quantity, RecipeStep
)
class ViewAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(IngredientCategory)
admin.site.register(Course)
# admin.site.register(Measurement)
admin.site.register(Blogger)
admin.site.register(Macronutrient)
# admin.site.register(Recipe)
# admin.site.register(Ingredient)
# admin.site.register(Quantity)
# admin.site.register(RecipeStep)
# admin.site.register(RecipeDescription)
