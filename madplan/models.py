import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class IngredientCategory(models.Model):
    ingredient_category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.ingredient_category_name

    class Meta:
        verbose_name_plural = "IngredientCategories"


class Course(models.Model):
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return self.course_name


class Measurement(models.Model):

    measurement_name = models.CharField(max_length=30)
    gram_equivalent = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.measurement_name

    class Meta:
        verbose_name_plural = "Measurements"


class Blogger(models.Model):
    blogger_name = models.CharField(max_length=50)

    def __str__(self):
        return self.blogger_name


class Macronutrient(models.Model):
    macronutrient_name = models.CharField(max_length=30)
    energy_content = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.macronutrient_name

    class Meta:
        verbose_name_plural = "Macronutrients"


class RecipeDescription(models.Model):
    recipe_headline = models.CharField(max_length=50)
    recipe_description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.recipe_headline

    class Meta:
        verbose_name_plural = "RecipeDescriptions"


class Recipe(models.Model):
    course = models.ManyToManyField(Course)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    recipe_description = models.OneToOneField(
        RecipeDescription, on_delete=models.CASCADE, default=None
    )
    recipe_name = models.CharField(max_length=80)
    cuisine = models.CharField(max_length=30)
    prep_time = models.IntegerField(null=True)
    cook_time = models.IntegerField(null=True)

    def __str__(self):
        return self.recipe_name

    class Meta:
        ordering = ["recipe_name"]


class Ingredient(models.Model):
    ingredient_category = models.ForeignKey(
        IngredientCategory, on_delete=models.CASCADE, null=True
    )
    ingredient_name = models.CharField(max_length=80)
    energy_content_Kcal = models.FloatField(null=True)
    protein_content_g = models.FloatField(null=True)
    carbohydrate_content_g = models.FloatField(null=True)
    fat_content_g = models.FloatField(null=True)
    fibre_content_g = models.FloatField(null=True)
    alcohol_content_g = models.FloatField(null=True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name_plural = "Ingredients"


class Quantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None)
    ingredient = models.ManyToManyField(Ingredient)
    measurement = models.ManyToManyField(Measurement)
    ingredient_quantity = models.FloatField(null=True)

    def __str__(self):
        return "{}".format(self.ingredient_quantity)

    class Meta:
        verbose_name_plural = "Quantities"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None)
    step_number = models.IntegerField()
    step_description = models.TextField(null=True)

    def __str__(self):
        return self.step_description

    class Meta:
        verbose_name_plural = "RecipeSteps"

