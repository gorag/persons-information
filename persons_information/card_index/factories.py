from datetime import timedelta

import factory
from factory import fuzzy

from . import models


class PersonsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Person

    gender = fuzzy.FuzzyChoice(choices=['MALE', 'FEMALE'])
    full_name = factory.LazyAttribute(
        lambda o:
        factory.Faker('name_male', 'ru_RU').generate({})
        if o.gender == 'MALE'
        else factory.Faker('name_female', 'ru_RU').generate({})
    )
    date_of_birth = factory.Faker('date_of_birth', 'ru_RU', minimum_age=16, maximum_age=60)
    phone_number = factory.Faker('phone_number', 'ru_RU')
    start_date = factory.LazyAttribute(
        lambda o:
        factory.Faker(
            'date_between_dates',
            'ru_RU',
            date_start=o.date_of_birth + timedelta(days=365 * 16)
        ).generate({})
    )
    end_date = factory.LazyAttribute(
        lambda o:
        factory.Faker(
            'date_between_dates',
            'ru_RU',
            date_start=o.date_start
        ).generate({})
    )
    training_group = factory.Faker('sentence', 'ru_RU', nb_words=3)
    educational_institution = factory.Faker('sentence', 'ru_RU', nb_words=3)
