from django.db import models

# Create your models here.


class Planet(models.Model):
    name = models.CharField("Nombre", max_length=200, blank=True)
    climate = models.CharField("Clima", max_length=200, blank=True)
    diameter = models.CharField("Diametro", max_length=200, blank=True)
    population = models.CharField(
        "Población", max_length=20, default="Prueba", blank=True
    )
    create_at = models.DateTimeField("fecha de creación", auto_now_add=True)
    update_at = models.DateTimeField("fecha de actualización", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Planeta"
        verbose_name_plural = "Planetas"


class Film(models.Model):
    title = models.CharField("Título", max_length=200, blank=True)
    episode_id = models.CharField("Id Episodio", max_length=2, blank=True)
    text_detail = models.CharField("Texto apertura", max_length=1200, blank=True)
    director = models.CharField("Director", max_length=200, blank=True)
    producer = models.CharField("Productor", max_length=200, blank=True)
    release_date = models.DateField("Fecha de lanzamiento", blank=True)
    planets = models.ManyToManyField(Planet, verbose_name="Panetas")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField("Nombre", max_length=200, blank=True)
    gender = models.CharField("Género", max_length=200, blank=True)
    height = models.CharField("Altura", max_length=3, blank=True)
    mass = models.CharField("Peso", max_length=3, blank=True)
    films = models.ManyToManyField(Film, verbose_name="Películas")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"

    def __str__(self):
        return self.name
