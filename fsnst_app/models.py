from django.db import models
from datetime import date


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    head = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null = True, blank=True, related_name='head',
                                   verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    code = models.CharField(max_length=10, verbose_name="Код")
    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=255, verbose_name="Ім'я координатора набору")
    coordinator_contact = models.CharField(max_length=255, verbose_name="Контакт координатора набору")

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='specialties',
                                   verbose_name="Випускова кафедра")
    disciplines = models.TextField(verbose_name="Список дисциплін")

    def __str__(self):
        return f"{self.code} - {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    position = models.CharField(max_length=255, verbose_name="Посада")
    degree = models.CharField(max_length=255, verbose_name="Ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers',
                                   verbose_name="Кафедра")

    def __str__(self):
        return self.name


class HomePageContent(models.Model):
    content = models.TextField(verbose_name="Текст головної сторінки")

    def __str__(self):
        return "Текст головної сторінки"

class ExchangeProgram(models.Model):
    university_name = models.CharField(max_length=255, verbose_name="Назва університету")
    country = models.CharField(max_length=100, verbose_name="Країна")
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    slots = models.CharField(max_length=50, verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")

    @property
    def is_open(self):
        return self.deadline >= date.today()

    def __str__(self):
        return f"{self.university_name} ({self.country})"