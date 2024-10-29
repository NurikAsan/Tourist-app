from django.db import models
from apps.common.model.mixin import Base


class PickupLocations(Base):
    latitude = models.FloatField(verbose_name="Широта", blank=True, null=True)
    longitude = models.FloatField(verbose_name="Долгота", blank=True, null=True)

    class Meta:
        verbose_name = "Точка сбора"
        verbose_name_plural = "Точки сбора"


class Category(Base):
    title = models.CharField(max_length=25, verbose_name='Категория')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Program(Base):
    verbose_name = 'Программа'
    time = models.CharField(max_length=100, null=True, verbose_name="Время")

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class Equipment(Base):
    verbose_name = 'Экипировка'

    class Meta:
        verbose_name = "Экипировка"
        verbose_name_plural = "Экипировки"


class Included(Base):
    verbose_name = "Входит в cтоимость"

    class Meta:
        verbose_name = "Входит в стоимость"
        verbose_name_plural = "Входят в стоимость"


class NotIncluded(Base):
    verbose_name = "Не входит в стоимость"

    class Meta:
        verbose_name = "Не входит в стоимость"
        verbose_name_plural = "Не входят в стоимость"


class Duration(Base):
    verbose_name = 'Длительность тура'

    class Meta:
        verbose_name = 'Длительность'
        verbose_name_plural = 'Длительности'


class Tour(models.Model):
    DIFFICULT = [
        (0, 'Easy'),
        (1, 'Middle'),
        (2, 'Hard')
    ]

    title = models.CharField(max_length=50, verbose_name="Название Тура")
    point = models.CharField(max_length=50, verbose_name="Точка(Местоположение)")
    description = models.TextField(verbose_name="Описание", max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    start_date = models.DateField(null=True, verbose_name='Дата начала')
    end_date = models.DateField(null=True, verbose_name='Дата окончания')
    views = models.PositiveBigIntegerField(default=0, verbose_name='Просмотры')
    archived = models.BooleanField(default=False, verbose_name='Архивирован')
    is_favorite = models.BooleanField(default=False, verbose_name='В избранное')

    pickup_locations = models.ManyToManyField(PickupLocations, verbose_name='Точки сбора')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Категория")
    program = models.ManyToManyField(Program, verbose_name="Программа тура")
    equipment = models.ManyToManyField(Equipment, verbose_name="Экипировка тура")
    included = models.ManyToManyField(Included, verbose_name="Что входит в стоимость")
    not_included = models.ManyToManyField(NotIncluded, verbose_name="Что не входит в стоимость")
    duration = models.ForeignKey(Duration, on_delete=models.DO_NOTHING, verbose_name="Длительность тура")
    difficulty = models.PositiveSmallIntegerField(
        choices=DIFFICULT, default=DIFFICULT[0][0],
        max_length=2, verbose_name="Сложность"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
