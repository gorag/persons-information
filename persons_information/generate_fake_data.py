if __name__ == "__main__":
    import os
    import sys

    sys.path.extend(sys.path[0])

    if len(sys.argv) == 1:
        num_records = 100
    else:
        num_records = int(sys.argv[1])

    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persons_information.settings')

    django.setup()
    from card_index.models import Person
    from card_index.factories import PersonsFactory

    Person.objects.bulk_create(PersonsFactory.build_batch(num_records))
