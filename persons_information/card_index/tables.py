import django_tables2 as tables

from .models import Person


class PersonTable(tables.Table):
    passport = tables.Column(empty_values=(), verbose_name='Паспорт')
    delete = tables.TemplateColumn('<a href="{{ record.get_absolute_url }}" class="btn btn-default">Подробнее</a>', verbose_name='')

    def render_passport(self, record):
        if record.documents.exists():
            return ', '.join([p.number if p.type == 'PASSPORT' else '' for p in record.documents.all()])
        return ''

    class Meta:
        model = Person
        fields = ('full_name', 'date_of_birth', 'gender', 'phone_number', 'start_date', 'end_date', 'training_group',
                  'educational_institution', 'passport')
        template_name = 'django_tables2/bootstrap-responsive.html'
