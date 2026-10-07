from django.db import models


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

