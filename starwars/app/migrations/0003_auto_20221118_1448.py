# Generated by Django 4.1.3 on 2022-11-18 14:48

from django.db import migrations
from app.models import Planet


def add_planets(apps, schema_editor):

    planets = [
        {
            "name": "Tatooine",
            "diameter": "10465",
            "climate": "arid",
            "population": "200000",
        },
        {
            "name": "Alderaan",
            "diameter": "12500",
            "climate": "temperate",
            "population": "2000000000",
        },
        {
            "name": "Yavin IV",
            "diameter": "10200",
            "climate": "temperate, tropical",
            "population": "1000",
        },
        {
            "name": "Hoth",
            "diameter": "7200",
            "climate": "frozen",
            "population": "unknown",
        },
        {
            "name": "Dagobah",
            "diameter": "8900",
            "climate": "murky",
            "surface_water": "8",
            "population": "unknown",
        },
        {
            "name": "Bespin",
            "diameter": "118000",
            "climate": "temperate",
            "population": "6000000",
        },
        {
            "name": "Endor",
            "diameter": "4900",
            "climate": "temperate",
            "population": "30000000",
        },
        {
            "name": "Naboo",
            "diameter": "12120",
            "climate": "temperate",
            "population": "4500000000",
        },
        {
            "name": "Coruscant",
            "diameter": "12240",
            "climate": "temperate",
            "population": "1000000000000",
        },
        {
            "name": "Kamino",
            "diameter": "19720",
            "climate": "temperate",
            "population": "1000000000",
        },
        {
            "name": "Geonosis",
            "diameter": "11370",
            "climate": "temperate, arid",
            "population": "100000000000",
        },
        {
            "name": "Utapau",
            "diameter": "12900",
            "climate": "temperate, arid, windy",
            "population": "95000000",
        },
        {
            "name": "Mustafar",
            "diameter": "4200",
            "climate": "hot",
            "population": "20000",
        },
    ]

    for planet in planets:
        new_planet = Planet(
            name=planet["name"],
            diameter=planet["diameter"],
            climate=planet["climate"],
            population=planet["population"],
        )
        new_planet.save()


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_initial"),
    ]

    operations = [migrations.RunPython(add_planets)]
