from django.shortcuts import render
from django.http import HttpResponse
from madplan.models import Recipe


def morgenmad(request):
    recipes = Recipe.objects.all()

    return render(request, "madplan/morgenmad.html", {"recipes": recipes})
