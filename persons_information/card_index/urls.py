from django.urls import path

from card_index import views
from card_index.views import persons

urlpatterns = [
    path('', persons, name='persons'),
    path('detail/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
]
