from django.db import models
from django.urls import reverse


class Person(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    GENDER = (
        ('MALE', 'мужской'),
        ('FEMALE', 'женский'),
    )

    gender = models.CharField(max_length=6, choices=GENDER, verbose_name='Пол')
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Номер мобильного телефона',
    )
    start_date = models.DateField(null=True, blank=True, verbose_name='Срок обучения с')
    end_date = models.DateField(null=True, blank=True, verbose_name='Срок обучения по')
    training_group = models.CharField(max_length=200, blank=True, verbose_name='Группа обучения')
    educational_institution = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Наименование учебного заведения',
    )

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Список персон'


class Document(models.Model):
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    date_of_issue = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')

    TYPE = (
        ('PASSPORT', 'Паспорт'),
        ('BIRTH_CERTIFICATE', 'Свидетельство о рождении'),
        ('DRIVERS_LICENSE', 'Водительское удостоверение'),
        ('STUDENT_CARD', 'Студенческий билет'),
    )

    type = models.CharField(max_length=30, choices=TYPE, default='PASSPORT', verbose_name='Тип')
    scan_document = models.FileField(
        upload_to='documents',
        null=True,
        blank=True,
        verbose_name='Скан документа'
    )
    person = models.ForeignKey(
        Person,
        related_name='documents',
        on_delete=models.CASCADE,
        verbose_name='Персона',
    )

    def __str__(self):
        return self.get_type_display() + ': ' + self.number

    def get_absolute_url(self):
        return reverse('document-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
